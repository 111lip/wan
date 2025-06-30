import rasterio
import numpy as np
from rasterio.enums import Resampling
from rasterio.plot import reshape_as_image
import matplotlib.pyplot as plt
import os

# 输入文件路径
input_tif = "2020_0427_fire_B2348_B12_10m_roi.tif"

# 输出文件路径
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
output_rgb = os.path.join(output_dir, "rgb_image.tif")
output_vis = os.path.join(output_dir, "rgb_visualization.jpg")

# 读取影像数据
with rasterio.open(input_tif) as src:
    # 获取元数据
    profile = src.profile
    print(f"影像波段数: {src.count}")
    print(f"影像宽度: {src.width}")
    print(f"影像高度: {src.height}")

    # 读取所有波段数据
    img_data = src.read()  # 维度顺序: (波段数, 高度, 宽度)

    # 打印各波段统计信息
    for band_idx in range(src.count):
        band_data = img_data[band_idx]
        print(
            f"波段 {band_idx + 1}: 最小值={np.min(band_data)}, 最大值={np.max(band_data)}, 均值={np.mean(band_data):.2f}")

# 定义波段索引（假设波段顺序为 B2,B3,B4,B8,B12）
BLUE_BAND = 0  # 对应 B2 (蓝)
GREEN_BAND = 1  # 对应 B3 (绿)
RED_BAND = 2  # 对应 B4 (红)

# 提取 RGB 波段
rgb_data = img_data[[RED_BAND, GREEN_BAND, BLUE_BAND], :, :]


# 数据压缩函数 - 将 0-10000 压缩到 0-255
def compress_to_8bit(data, min_val=0, max_val=10000):
    """将 16 位数据压缩到 8 位 (0-255)"""
    # 裁剪数据到指定范围
    clipped = np.clip(data, min_val, max_val)
    # 线性拉伸到 0-255
    compressed = ((clipped - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    return compressed


# 对 RGB 数据进行压缩
rgb_compressed = np.zeros_like(rgb_data, dtype=np.uint8)
for i in range(3):
    rgb_compressed[i] = compress_to_8bit(rgb_data[i])

# 保存 RGB 图像（保持栅格格式）
profile.update(
    dtype=rasterio.uint8,
    count=3,
    photometric='RGB'
)

with rasterio.open(output_rgb, 'w', **profile) as dst:
    dst.write(rgb_compressed)
    print(f"RGB 图像已保存至: {output_rgb}")

# 可视化并保存预览图（用于快速查看）
rgb_image = reshape_as_image(rgb_compressed)  # 调整为 (高度, 宽度, 波段)
plt.figure(figsize=(10, 10))
plt.imshow(rgb_image)
plt.title("Sentinel-2 RGB Composite")
plt.axis('off')
plt.savefig(output_vis, dpi=300, bbox_inches='tight')
plt.close()
print(f"RGB 可视化预览图已保存至: {output_vis}")

print("\n处理完成！")
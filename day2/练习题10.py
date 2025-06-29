import numpy as np

# 创建数组 A：3x2 的二维数组，元素为 1 到 6
array_a = np.arange(1, 7).reshape(3, 2)
# 创建数组 B：一维数组，包含元素 [10, 20]
array_b = np.array([10, 20])

# 任务 1：计算 A 和 B 的逐元素相加（利用广播）
addition_result = array_a + array_b
print("任务 1：A 和 B 逐元素相加结果：")
print(addition_result)
print()

# 任务 2：计算 A 和 B 的逐元素相乘（利用广播）
multiplication_result = array_a * array_b
print("任务 2：A 和 B 逐元素相乘结果：")
print(multiplication_result)
print()

# 任务 3：计算 A 的每一行与 B 的点积
# 方法 1：手动遍历行计算点积（适合理解过程）
dot_product_manual = []
for row in array_a:
    dot_product_manual.append(np.dot(row, array_b))
dot_product_manual = np.array(dot_product_manual)

# 方法 2：利用广播和 sum 简化计算（更高效）
dot_product_efficient = np.sum(array_a * array_b, axis=1)

print("任务 3：A 的每一行与 B 的点积（手动遍历）：")
print(dot_product_manual)
print("任务 3：A 的每一行与 B 的点积（广播简化）：")
print(dot_product_efficient)
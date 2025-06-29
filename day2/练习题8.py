import numpy as np

# 创建 3x4 的二维数组，元素为 1 到 12 的整数
arr = np.arange(1, 13).reshape(3, 4)

# 1. 打印数组的形状、维度和数据类型
print("数组的形状:", arr.shape)
print("数组的维度:", arr.ndim)
print("数组的数据类型:", arr.dtype)

# 2. 将数组元素乘以 2，打印结果
arr_doubled = arr * 2
print("数组元素乘以 2 的结果:\n", arr_doubled)

# 3. 将数组重塑为 4x3 的形状，打印新数组
arr_reshaped = arr.reshape(4, 3)
print("数组重塑为 4x3 后的结果:\n", arr_reshaped)
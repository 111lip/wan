import numpy as np

# 给定 4x4 数组
array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

# 任务 1：提取第 2 行所有元素
row_2 = array[1, :]
print("任务 1 - 第 2 行所有元素：")
print(row_2)
print()

# 任务 2：提取第 3 列所有元素
col_3 = array[:, 2]
print("任务 2 - 第 3 列所有元素：")
print(col_3)
print()

# 任务 3：提取子数组（包含第 1、2 行和第 2、3 列）
sub_array = array[:2, 1:3]
print("任务 3 - 子数组（第 1、2 行和第 2、3 列）：")
print(sub_array)
print()

# 任务 4：将大于 10 的元素替换为 0，打印修改后的数组
modified_array = array.copy()
modified_array[modified_array > 10] = 0
print("任务 4 - 大于 10 的元素替换为 0 后的数组：")
print(modified_array)
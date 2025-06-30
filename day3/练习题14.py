import pandas as pd
import numpy as np

# 创建包含数据的字典
data = {
    'Student_ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', None, 'David', 'Ella'],  # Name 列包含 1 个空值
    'Score': [85, 92, np.nan, 78, 88],  # Score 列包含 1 个空值（np.nan）
    'Grade': ['A', 'A', 'B', 'B', 'A']
}

# 创建 DataFrame
df = pd.DataFrame(data)

# 保存为 students.csv 文件，设置 index=False 避免写入索引列
df.to_csv('students.csv', index=False)
print("已创建 students.csv 文件")
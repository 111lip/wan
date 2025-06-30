import pandas as pd

# 文件路径列表，根据实际情况调整
file_paths = [
    "2015年国内主要城市年度数据.csv",
    "2016年国内主要城市年度数据.csv",
    "2017年国内主要城市年度数据.csv"
]

# 1. 合并数据，纵向连接
dfs = []
for file in file_paths:
    df = pd.read_csv(file)
    # 添加年份列（从文件名提取）
    year = int(file.split("年")[0])
    df["年份"] = year
    dfs.append(df)

merged_df = pd.concat(dfs, axis=0, ignore_index=True)

# 调试：查看列名
print("数据列名:", merged_df.columns.tolist())

# 2. 处理缺省值，填充为0
merged_df.fillna(0, inplace=True)

# 3. 按照年份聚合，求每年的国内生产总值
# 请将 "国内生产总值" 替换为实际列名
annual_gdp = merged_df.groupby("年份")["国内生产总值"].sum().reset_index()

# 4. 输出结果
print("\n合并后的数据前几行：")
print(merged_df.head().to_csv(sep="\t", na_rep="nan"))
print("\n每年的国内生产总值：")
print(annual_gdp.to_csv(sep="\t", na_rep="nan"))
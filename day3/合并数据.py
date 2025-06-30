import pandas as pd
import numpy as np

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

# 3. 按照年份聚合，求每年的国内生产总值（需根据实际列名调整，这里假设为“国内生产总值” ）
annual_gdp = merged_df.groupby("年份")["国内生产总值"].sum().reset_index()
print("\n每年的国内生产总值：")
print(annual_gdp)

# 5. 计算每个城市2015 - 2017年GDP的年均增长率，并找出增长率最高和最低的五个城市
def calculate_gdp_growth_rate(df, gdp_column="国内生产总值", city_column="地区", year_column="年份"):
    try:
        # 筛选2015和2017年的数据（假设存在这些年份数据 ，若数据年份不同需调整）
        gdp_2015 = df[df[year_column] == 2015].set_index(city_column)[gdp_column].rename("GDP_2015")
        gdp_2017 = df[df[year_column] == 2017].set_index(city_column)[gdp_column].rename("GDP_2017")

        # 合并两年的数据
        gdp_comparison = pd.concat([gdp_2015, gdp_2017], axis=1)

        # 计算年均增长率：((GDP_2017/GDP_2015)^(1/2) - 1) * 100% ，这里假设是两年间隔，按实际年份差调整指数
        gdp_comparison['年均增长率(%)'] = ((gdp_comparison['GDP_2017'] / gdp_comparison['GDP_2015']) ** (1 / 2) - 1) * 100

        # 找出增长率最高和最低的五个城市
        top_five = gdp_comparison.nlargest(5, '年均增长率(%)')
        bottom_five = gdp_comparison.nsmallest(5, '年均增长率(%)')

        return gdp_comparison, top_five, bottom_five
    except KeyError as e:
        print(f"计算年均增长率时列未找到：{e}，请检查列名是否正确")
        return None, None, None


# 执行计算（需确保列名正确，这里假设城市列名为“城市” ，可根据实际调整）
gdp_growth, top_cities, bottom_cities = calculate_gdp_growth_rate(merged_df, city_column="城市")
if gdp_growth is not None:
    print("\n5. 年均增长率最高的五个城市:")
    print(top_cities[['GDP_2015', 'GDP_2017', '年均增长率(%)']].round(2))
    print("\n年均增长率最低的五个城市:")
    print(bottom_cities[['GDP_2015', 'GDP_2017', '年均增长率(%)']].round(2))

# 6. 对医院、卫生院数进行归一化处理（Min - Max标准化），并按年份比较各城市医疗资源的变化
def normalize_hospital_data(df, hospital_column="医院、卫生院数", city_column="城市", year_column="年份"):
    try:
        # 创建一个副本，避免修改原始数据
        normalized_df = df.copy()

        # 按年份进行Min - Max标准化
        normalized_df['医院、卫生院数_归一化'] = 0.0  # 初始化新列

        for year in normalized_df[year_column].unique():
            year_data = normalized_df[normalized_df[year_column] == year]
            min_val = year_data[hospital_column].min()
            max_val = year_data[hospital_column].max()

            # 标准化公式：(x - min) / (max - min)
            if max_val != min_val:  # 避免除以零
                normalized_df.loc[normalized_df[year_column] == year, '医院、卫生院数_归一化'] = \
                    (year_data[hospital_column] - min_val) / (max_val - min_val)

        # 计算每个城市医疗资源的变化（2017年与2015年的差值，年份按需调整）
        normalized_2015 = normalized_df[normalized_df[year_column] == 2015].set_index(city_column)['医院、卫生院数_归一化'].rename("归一化_2015")
        normalized_2017 = normalized_df[normalized_df[year_column] == 2017].set_index(city_column)['医院、卫生院数_归一化'].rename("归一化_2017")

        change = pd.concat([normalized_2015, normalized_2017], axis=1)
        change['变化量'] = change['归一化_2017'] - change['归一化_2015']

        return normalized_df, change
    except KeyError as e:
        print(f"归一化医疗资源数据时列未找到：{e}，请检查列名是否正确")
        return None, None


# 执行归一化（需确保医院数量列名正确，假设为“医院、卫生院数” ，城市列名为“城市” ）
normalized_df, hospital_change = normalize_hospital_data(merged_df, city_column="城市")
if normalized_df is not None and hospital_change is not None:
    print("\n6. 医疗资源变化最大的五个城市:")
    print(hospital_change.nlargest(5, '变化量').round(4))
    print("\n医疗资源变化最小的五个城市:")
    print(hospital_change.nsmallest(5, '变化量').round(4))

# 7. 提取北京、上海、广州、深圳四个城市2015 - 2017的GDP和社会商品零售总额数据，用新的csv呈现
def extract_special_cities(df, cities=['北京', '上海', '广州', '深圳'],
                           gdp_column="国内生产总值", retail_column="社会商品零售总额",
                           year_column="年份", city_column="城市"):
    try:
        # 筛选指定城市和年份的数据
        filtered_df = df[(df[city_column].isin(cities)) & (df[year_column].isin([2015, 2016, 2017]))]

        # 提取需要的列
        result_df = filtered_df[[city_column, year_column, gdp_column, retail_column]]

        # 保存为新的CSV文件
        output_file = "北上广深经济数据.csv"
        result_df.to_csv(output_file, index=False, encoding="utf-8-sig")

        print(f"\n7. 已将数据保存到 {output_file}")
        return result_df
    except KeyError as e:
        print(f"提取特定城市数据时列未找到：{e}，请检查列名是否正确")
        return None


# 执行提取（需确保各列名正确 ）
special_cities_data = extract_special_cities(merged_df, city_column="城市")
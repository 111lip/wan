import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2_contingency
from textwrap import wrap

# ======================
# 1. 数据准备
# ======================
# 读取数据（请替换为您的实际路径）
try:
    data = pd.read_csv(r'C:\Users\Lenovo\PycharmProjects\pythonProject\day4\train.csv')
except FileNotFoundError:
    print("文件未找到，请检查路径！")
    exit()

# 数据质量检查
print("原始数据形状:", data.shape)
print("\n缺失值统计:")
print(data[['Age', 'Sex', 'Survived']].isnull().sum())

# ======================
# 2. 数据清洗
# ======================
# 删除关键字段缺失值
data_clean = data.dropna(subset=['Age', 'Sex', 'Survived']).copy()

# 年龄异常值处理
data_clean = data_clean[(data_clean['Age'] > 0) & (data_clean['Age'] <= 100)]
print("\n清洗后数据形状:", data_clean.shape)

# ======================
# 3. 数据分组与统计
# ======================
# 科学年龄分组
bins = [0, 12, 18, 30, 50, 65, 100]
labels = [
    '儿童(0-12岁)',
    '青少年(13-18岁)',
    '青壮年(19-30岁)',
    '中年(31-50岁)',
    '中老年(51-65岁)',
    '老年人(65+岁)'
]

data_clean['AgeGroup'] = pd.cut(
    data_clean['Age'],
    bins=bins,
    labels=labels,
    right=False
)

# 确保所有年龄组都有数据
all_combinations = pd.MultiIndex.from_product(
    [['male', 'female'], labels],
    names=['Sex', 'AgeGroup']
)

# 计算各分组生还率
result = data_clean.groupby(['Sex', 'AgeGroup'])['Survived'].agg(
    Survived_Count='sum',
    Total_Count='count'
).reindex(all_combinations).fillna(0).reset_index()

result['Survival Rate'] = round((result['Survived_Count'] / result['Total_Count'].replace(0, 1)) * 100, 1)

# ======================
# 4. 高级可视化
# ======================
plt.figure(figsize=(16, 8))
plt.style.use('ggplot')  # 使用可用的样式

# 颜色设置
male_color = '#3498db'  # 蓝色
female_color = '#e74c3c'  # 红色
overall_color = '#2ecc71'  # 绿色

# 分组柱状图参数
x = np.arange(len(labels))
width = 0.4
gap = 0.1

# 准备绘图数据
male_data = result[result['Sex'] == 'male'].sort_values('AgeGroup')
female_data = result[result['Sex'] == 'female'].sort_values('AgeGroup')

# 绘制男性生还率
bars_male = plt.bar(
    x - width/2 - gap/2,
    male_data['Survival Rate'],
    width=width,
    label='男性',
    color=male_color,
    edgecolor='white',
    linewidth=1,
    alpha=0.9,
    zorder=3
)

# 绘制女性生还率
bars_female = plt.bar(
    x + width/2 + gap/2,
    female_data['Survival Rate'],
    width=width,
    label='女性',
    color=female_color,
    edgecolor='white',
    linewidth=1,
    alpha=0.9,
    zorder=3
)

# 添加数据标签
def add_labels(bars, rotation=0):
    for bar in bars:
        height = bar.get_height()
        if height > 0:  # 只为正值添加标签
            plt.text(
                bar.get_x() + bar.get_width()/2,
                height + 1,
                f'{height}%',
                ha='center',
                va='bottom',
                fontsize=10,
                rotation=rotation,
                fontweight='bold'
            )

add_labels(bars_male)
add_labels(bars_female, rotation=45)

# 参考线和整体统计
overall_rate = round(data_clean['Survived'].mean() * 100, 1)
sex_rates = data_clean.groupby('Sex')['Survived'].mean() * 100

plt.axhline(
    y=overall_rate,
    color=overall_color,
    linestyle='--',
    linewidth=2,
    alpha=0.7,
    label=f'整体生还率 ({overall_rate}%)',
    zorder=2
)

# 图表装饰
plt.xlabel('年龄组', fontsize=12, labelpad=10)
plt.ylabel('生还率 (%)', fontsize=12, labelpad=10)
title = "泰坦尼克号乘客生还率分析：性别与年龄的影响"
plt.title('\n'.join(wrap(title, width=50)), fontsize=14, pad=20)
plt.xticks(x, labels, rotation=45, ha='right')
plt.ylim(0, 110)

# 图例
plt.legend(
    loc='upper right',
    frameon=True,
    framealpha=0.9,
    shadow=True,
    borderpad=1
)

# 美化图表
plt.grid(axis='y', linestyle=':', alpha=0.4, zorder=0)
plt.gca().set_facecolor('#f8f9fa')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()

plt.show()

# ======================
# 5. 补充分析
# ======================
print("\n=== 关键统计 ===")
print(f"整体生还率: {overall_rate}%")
print(f"女性生还率: {round(sex_rates['female'], 1)}%")
print(f"男性生还率: {round(sex_rates['male'], 1)}%")

highest_group = result.loc[result['Survival Rate'].idxmax()]
print(f"\n生还率最高的群体: {highest_group['Sex']}-{highest_group['AgeGroup']} ({highest_group['Survival Rate']}%)")

lowest_group = result.loc[result['Survival Rate'].idxmin()]
print(f"生还率最低的群体: {lowest_group['Sex']}-{lowest_group['AgeGroup']} ({lowest_group['Survival Rate']}%)")

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 设置中文字体（Windows系统用"SimHei"，Mac用"Arial Unicode MS"）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 替换为你系统已有的中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 模拟数据
data = {
    '城市': ['北京', '上海', '广州', '深圳', '重庆'],
    '2015': [24500, 25100, 18100, 17500, 16100],
    '2016': [25600, 27400, 19600, 19400, 17600],
    '2017': [28000, 30100, 21500, 22200, 19500]
}
df = pd.DataFrame(data)

# 1. 绘制2015-2017年各个城市的国内生产总值的柱状图（更适合比较）
plt.figure(figsize=(10, 6))
x = np.arange(len(df['城市']))
width = 0.25

plt.bar(x - width, df['2015'], width, label='2015', color='#1f77b4')
plt.bar(x, df['2016'], width, label='2016', color='#ff7f0e')
plt.bar(x + width, df['2017'], width, label='2017', color='#2ca02c')

plt.xlabel('城市')
plt.ylabel('GDP (亿元)')
plt.title('2015-2017年各城市GDP对比')
plt.xticks(x, df['城市'])
plt.legend()

# 添加数据标签
for i in x:
    for year, offset in zip(['2015', '2016', '2017'], [-width, 0, width]):
        plt.text(i + offset, df[year][i] + 100, f'{df[year][i]}',
                ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()

# 2. 绘制2015年各个城市的国内生产总值的饼状图
plt.figure(figsize=(10, 8))
plt.pie(df['2015'], labels=df['城市'], autopct='%1.1f%%',
        startangle=90, shadow=True, explode=(0.1, 0, 0, 0, 0))
plt.title('2015年各城市GDP占比')
plt.axis('equal')  # 使饼图为正圆形
plt.tight_layout()
plt.show()
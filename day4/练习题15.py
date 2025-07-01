import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号
plt.rcParams["font.family"] = ["SimHei"]
# 国家
countries = ['挪威', '德国', '中国', '美国', '瑞典']
# 金牌个数
gold_medal = np.array([16, 12, 9, 8, 8])
# 银牌个数
silver_medal = np.array([8, 10, 4, 10, 5])
# 铜牌个数
bronze_medal = [13, 5, 2, 7, 5]

x = np.arange(len(countries))
# 恢复 X 轴的坐标值
plt.xticks(x, countries)

# 绘图
plt.bar(x - 0.2, gold_medal, width=0.2, color="gold")
plt.bar(x, silver_medal, width=0.2, color="silver")
plt.bar(x + 0.2, bronze_medal, width=0.2, color="saddlebrown")

# 显示文本标签
# 金牌
for i in x:
    plt.text(x[i] - 0.2, gold_medal[i], gold_medal[i],
             va='bottom', ha='center', fontsize=8)
# 银牌
for i in x:
    plt.text(x[i], silver_medal[i], silver_medal[i],
             va='bottom', ha='center', fontsize=8)
# 铜牌
for i in x:
    # 修正这里的参数，bronze_medal 是列表，通过索引取值
    plt.text(x[i] + 0.2, bronze_medal[i], bronze_medal[i],
             va='bottom', ha='center', fontsize=8)

# 添加标题和坐标轴标签（可选，让图表更清晰）
plt.title("各国奖牌数量分布")
plt.xlabel("国家")
plt.ylabel("奖牌数量")

# 显示图表
plt.show()

# 实训日志 - 第四天

## 📅 日期：2025年7月1日  
**今日主题**：Jupyter高级可视化 & 深度学习入门  

## 一、核心学习内容

### 1. Jupyter高级数据可视化
#### 1.1 饼图深度实践
- 使用`matplotlib.pyplot.pie()`绘制基础饼图
- 关键参数解析：
  ```python
  plt.pie(sizes, 
         labels=labels,
         autopct='%1.1f%%',
         shadow=True,
         explode=(0.1,0,0,0))  # 突出第一区块
环形饼图实现技巧：
plt.pie(sizes, radius=1, wedgeprops=dict(width=0.3))
1.2 其他重要图表
图表类型	适用场景	示例API
热力图	相关性分析	sns.heatmap(corr_matrix)
箱线图	异常值检测	df.boxplot(column='Age')
小提琴图	分布对比	sns.violinplot(x='Class',y='Age')
2. 泰坦尼克号项目深化
2.1 特征工程优化
新增衍生特征：

python
df['Title'] = df.Name.str.extract(' ([A-Za-z]+)\.')
df['Deck'] = df.Cabin.str[0]
特征重要性分析：

pd.Series(model.feature_importances_, 
         index=X.columns).sort_values().plot.barh()
3. 深度学习过渡
3.1 PyTorch环境配置
验证安装成功：

python
import torch
print(f"PyTorch版本：{torch.__version__}")
print(f"GPU可用：{torch.cuda.is_available()}")
重要概念速记：

张量(Tensor): 多维数组，支持GPU加速

三、学习反思
✅ 掌握要点
饼图各参数的灵活运用

PyTorch张量的核心操作方法

特征重要性可视化分析

❓ 待解决问题
环形饼图标签自动避让的实现

torch.nn.Module类的继承规范

四、明日计划
完成PyTorch线性回归实战

学习MNIST数据集加载

理解epoch/batch_size等超参数
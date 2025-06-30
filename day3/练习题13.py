import pandas as pd


# 读取数据文件
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"数据加载成功，共{df.shape[0]}行，{df.shape[1]}列")
        return df
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 不存在")
        return None
    except Exception as e:
        print(f"错误：加载文件时发生异常 - {e}")
        return None


# 问题1：哪个大陆平均消耗的啤酒更多
def question1(df):
    # 按大陆分组计算啤酒消耗量的均值
    beer_mean_by_continent = df.groupby('continent')['beer_servings'].mean()
    # 找出最大值对应的大陆
    max_beer_continent = beer_mean_by_continent.idxmax()
    max_beer_value = beer_mean_by_continent.max()

    print("\n问题1：哪个大陆平均消耗的啤酒更多？")
    print(f"答案：{max_beer_continent}，平均啤酒消耗量为 {max_beer_value:.2f}")
    return beer_mean_by_continent


# 问题2：打印出每个大陆的红酒消耗的描述性统计值
def question2(df):
    # 按大陆分组计算红酒消耗量的描述性统计
    wine_stats_by_continent = df.groupby('continent')['wine_servings'].describe()

    print("\n问题2：每个大陆的红酒消耗的描述性统计值：")
    print(wine_stats_by_continent.to_markdown(numalign='left', stralign='left'))
    return wine_stats_by_continent


# 问题3：打印出每个大陆每种酒类别的消耗平均值
def question3(df):
    # 按大陆分组计算三种酒类的均值
    alcohol_mean_by_continent = df.groupby('continent')[['beer_servings', 'spirit_servings', 'wine_servings']].mean()

    print("\n问题3：每个大陆每种酒类别的消耗平均值：")
    print(alcohol_mean_by_continent.to_markdown(numalign='left', stralign='left'))
    return alcohol_mean_by_continent


# 问题4：打印出每个大陆每种酒类别的消耗中位数
def question4(df):
    # 按大陆分组计算三种酒类的中位数
    alcohol_median_by_continent = df.groupby('continent')[
        ['beer_servings', 'spirit_servings', 'wine_servings']].median()

    print("\n问题4：每个大陆每种酒类别的消耗中位数：")
    print(alcohol_median_by_continent.to_markdown(numalign='left', stralign='left'))
    return alcohol_median_by_continent


def main():
    file_path = 'drinks.csv'  # 请确保文件在正确路径下
    df = load_data(file_path)

    if df is not None:
        # 查看数据基本信息
        print("\n数据基本信息：")
        df.info()

        # 执行四个问题的分析
        question1(df)
        question2(df)
        question3(df)
        question4(df)


if __name__ == "__main__":
    main()
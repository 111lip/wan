import os
import pandas as pd
import time
import random
from serpapi import SerpApiClient  # 适用于 0.1.5 版本


def scrape_google_scholar(query, num_results=10, language="en", serpapi_api_key=None):
    """使用 SerpApi 爬取 Google 学术搜索结果（兼容 0.1.5 版本）"""
    if serpapi_api_key is None:
        serpapi_api_key = os.getenv("SERPAPI_API_KEY")
        if not serpapi_api_key:
            raise ValueError("需要提供 SerpAPI API 密钥")

    results = []
    start = 0

    while len(results) < num_results:
        params = {
            "engine": "google_scholar",
            "q": query,
            "hl": language,
            "start": start,
            "num": min(20, num_results - len(results)),
            "api_key": serpapi_api_key
        }

        # 模拟人类行为：随机延时
        time.sleep(random.uniform(2, 5))

        try:
            # 0.1.5 版本的初始化方式
            client = SerpApiClient(
                api_key=serpapi_api_key,
                engine="google_scholar"
            )

            # 0.1.5 版本的调用方式
            result_dict = client.get_json()  # 使用 get_json() 而非 get_dict()

            if "organic_results" in result_dict:
                for item in result_dict["organic_results"]:
                    result = {
                        "title": item.get("title", ""),
                        "link": item.get("link", ""),
                        "snippet": item.get("snippet", ""),
                        "publication_info": item.get("publication_info", {}).get("summary", ""),
                        "cited_by_count": item.get("inline_links", {}).get("cited_by", {}).get("total", 0),
                        "year": extract_year(item.get("publication_info", {}).get("summary", ""))
                    }
                    results.append(result)

            # 检查是否还有下一页
            if "pagination" not in result_dict or "next" not in result_dict["pagination"]:
                break

            start += 20

        except Exception as e:
            print(f"搜索出错: {e}")
            # 打印完整错误信息用于调试
            import traceback
            print(traceback.format_exc())
            break

    return pd.DataFrame(results)


def extract_year(publication_info):
    """从出版信息中提取年份"""
    import re
    match = re.search(r'\b(19|20)\d{2}\b', publication_info)
    return int(match.group(0)) if match else None


def simulate_human_behavior(df):
    """模拟人类浏览行为：随机查看某些结果"""
    if not df.empty:
        num_views = random.randint(2, 5)
        viewed_indices = random.sample(range(len(df)), min(num_views, len(df)))

        for idx in viewed_indices:
            result = df.iloc[idx]
            print(f"\n查看结果 #{idx + 1}: {result['title']}")
            print(f"链接: {result['link']}")
            print(f"发布信息: {result['publication_info']}")

            # 模拟阅读时间
            read_time = random.uniform(8, 20)
            print(f"阅读时间: {read_time:.1f}秒")
            time.sleep(read_time)


def main():
    # 设置 API 密钥（也可以通过环境变量设置）
    serpapi_api_key = "your_serpapi_api_key"

    # 搜索查询
    query = "machine learning"

    # 爬取结果
    print(f"正在搜索: '{query}'...")
    results_df = scrape_google_scholar(
        query=query,
        num_results=10,
        language="en",
        serpapi_api_key=serpapi_api_key
    )

    # 显示结果
    if not results_df.empty:
        print(f"\n找到 {len(results_df)} 条结果")
        print(results_df[["title", "year", "cited_by_count"]].to_markdown(numalign='left', stralign='left'))

        # 模拟人类浏览行为
        simulate_human_behavior(results_df)
    else:
        print("未找到搜索结果")


if __name__ == "__main__":
    main()
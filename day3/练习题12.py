import requests
from bs4 import BeautifulSoup
import time
import random
import pandas as pd


def get_movie_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
        return None


def parse_movie_data(html_content):
    if not html_content:
        return []

    soup = BeautifulSoup(html_content, 'html.parser')
    movie_list = []

    for item in soup.select('div.item')[:10]:  # 只取前10个
        try:
            rank = item.select_one('div.pic em').text.strip()
            title = item.select_one('span.title').text.strip()
            rating = item.select_one('span.rating_num').text.strip()
            quote = item.select_one('span.inq')
            quote = quote.text.strip() if quote else '暂无评价'

            movie_list.append({
                '排名': rank,
                '片名': title,
                '评分': rating,
                '评语': quote
            })
        except (AttributeError, ValueError) as e:
            print(f"解析出错: {e}")
            continue

    return movie_list


def main():
    base_url = 'https://movie.douban.com/top250'
    movie_data = []

    for start in range(0, 10, 25):  # 只取第一页的前10个
        url = f"{base_url}?start={start}"
        print(f"正在爬取: {url}")

        html_content = get_movie_info(url)
        movies = parse_movie_data(html_content)
        movie_data.extend(movies)

        # 随机延时，避免请求过于频繁
        time.sleep(random.uniform(1, 3))

    # 转换为DataFrame并保存
    df = pd.DataFrame(movie_data)

    # 打印结果
    print("\n豆瓣电影排名前十的电影:")
    print(df.to_markdown(numalign='left', stralign='left'))


if __name__ == "__main__":
    main()
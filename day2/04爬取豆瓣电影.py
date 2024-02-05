import json
import requests


if __name__ == '__main__':
    url = "https://movie.douban.com/j/chart/top_list"
    # 进行ua伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    # 参数
    params = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': 60,
        'limit': 20,
    }
    response = requests.get(url=url, headers=headers, params=params)
    if response.status_code == 200:
        result_dict = response.json()

    print(result_dict)


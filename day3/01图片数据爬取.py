'''
用正则进行数据解析
需求：爬取糗事百科中所有的图片
'''
import re
import requests


if __name__ == '__main__':
    url = 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2901534046.webp'
    # 进行ua伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url=url, headers=headers)

    # 返回二进制数据
    img_data = response.content

    with open('./haha.webp', 'wb') as fp:
        fp.write(img_data)
    print(img_data)
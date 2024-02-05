'''
反爬机制: UA检测
User-Agent: 网站会检测对应请求的载体身份标识，如果检测到请求的载体是某一款浏览器，则该请求是正常请求。
但是如果检测的不是浏览器的请求，则是不正常的请求。则为爬虫。

UA伪装： 伪装成某一款浏览器

'''

import requests


if __name__ == '__main__':
    # step1: 指定url
    url = "https://www.sogou.com/web?"
    # 封装到字典中，加入user-agent，字典
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    # 处理url携带的参数
    kw = input("enter a word:")
    params = {
        "query": kw
    }
    # step2: 发起请求
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        # step3: 获取响应数据，字符串形式
        page_text = response.text
        print(page_text)
        # step4: 持久化
        file_name = kw + '.html'
        with open(file_name, "w", encoding="utf-8") as fp:
            fp.write(page_text)
    else:
        print("请求失败")



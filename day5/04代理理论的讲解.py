'''
代理：
ip被封怎么办？
什么是代理：
    - 代理服务器：中转站
代理的作用：
    - 突破自身ip访问的限制。
代理相关的网站：
    - 快代理
    - 西祠代理
    - www.goubanjia.com
代理ip的类型：
    http: 
    https: 只能应用到
'''
import requests

# http_proxy=http://127.0.0.1:7890
if __name__ == '__main__':
    url = 'https://www.youtube.com/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    session = requests.Session()
    # 在get方法中，用proxies添加代理ip，分为http以及https
    response = session.get(url, headers=headers, proxies={"https": "http://127.0.0.1:7890"})
    if response.status_code == 200:
        print("successful!!!")
        page_text = response.text
        with open("./yutube.html", 'w') as fp:
            fp.write(page_text)
    else:
        print("false!!!")

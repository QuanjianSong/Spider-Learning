'''
基于网络请求的两个模块：
    urllib模块
    request模块: python中原生的基于网络请求的模块, 模拟浏览器发请求。

如何使用requests:
    - 指定url
    - 发起请求(get、post)
    - 获取响应数据
    - 响应数据的持久化存储



'''
import requests



if __name__ == '__main__':
    # step1: 指定url
    url = "https://www.sogou.com/"
    # step2: 发送请求
    response = requests.get(url)
    if response.status_code == 200:
        # step3: 获取相应数据
        page_text = response.text # .text返回的是字符串形式的响应数据。
        print(page_text)
    # step4: 持久话存储
    with open("./sougou.js", "w", encoding="utf-8") as fp:
        fp.write(page_text)
    print("爬去数据成功！！！")
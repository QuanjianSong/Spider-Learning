'''
post请求（携带了参数）
响应数据是一组json数据。
json数据可以用.json()方法
'''
import json
import requests


if __name__ == '__main__':
    # step1: 指定url
    post_url = "https://fanyi.baidu.com/sug"
    # 进行ua伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    # 用户输入：
    word = input("enter a world:")
    # 参数处理，同get中的params
    data = {
        'kw': word
    }
    
    # 同get请求
    response = requests.post(url=post_url, data=data, headers=headers)
    # .text返回字符串格式
    result_string = response.text
    # .json方法返回json的obj, 不是任何时候都能用，确认服务器返回的是json格式才可以。
    result_json = response.json()
    print(result_json)
    # 持久化存储
    fp = open(word + '.json', 'w')
    json.dump(result_json, fp=fp, ensure_ascii=False)





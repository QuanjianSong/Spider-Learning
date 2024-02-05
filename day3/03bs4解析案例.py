'''
bs4的数据解析原理: 
    - 实例化一个beautifulSoup的对象, 并且将页面源码数据加载到该对象中。
        1.将本地的html文档数据加载到该对象中
        2.将互联网中的html文档数据加载到该对象中
    - 通过调用BeautifulSoup对象中相关的属性进行提取
'''
from bs4 import BeautifulSoup
import requests


if __name__ == '__main__':
    # fp = open('.html', 'r')
    # soup = BeautifulSoup(fp, 'lxml')
    url = "https://movie.douban.com/"
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
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        result_dict = response.text
        soup = BeautifulSoup(result_dict, 'lxml') # 传入必须是字符串，不能是json。如果是json要手动转
        # print(soup)
        # 提供的用于数据解析的方法和属性
        # print(soup.div) # 返回文档中第一次出现的tag_name对应的标签
        # print(soup.find('div')) # 返回文档中第一次出现的tag_name对应的标签，相当于soup.div。
        # print(soup.find('div', class_="download").a.text) # 可以额外增加属性
        # print(len(soup.find_all('div'))) # 返回一个列表，所有匹配的结果
        print(soup.select('.download')[0].a['href'])

        '''
        select:
            soup.select('某种选择器'): 返回的是一个列表
            eg. soup.select('.tang > ul > li > a')
            eg. soup.select('.tang > ul a') 空格表示多个层级 
        
        获取标签之间的文本数据---> .text
        获取标签中的属性---> a.['href']
        '''
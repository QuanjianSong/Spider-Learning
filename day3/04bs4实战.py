'''
需求
url: www.shicimingju.com/book/sanguoyanyi.html
'''
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    print(response.encoding)
    if response.status_code == 200:
        page_text = response.text
        # print(page_text)
        
        # 在首页中解析出标题和详情页
        soup = BeautifulSoup(page_text, 'lxml')
        li_list = soup.select('.book-mulu > ul > li')
        for item in li_list:
            title = item.a.text
            detail_url = 'http://www.shicimingju.com' + item.a['href']
            # print(detail_url)
            # 对详情页面发起请求
            detail_page_text = requests.get(url=detail_url, headers=headers).text
            # print(detail_page_text)
            # 解析出详情页的相关章节的内容
            detail_soup = BeautifulSoup(detail_page_text, 'lxml')
            detail_list = detail_soup.select('.chapter_content > p')
            for text in detail_list:
                print(text.text)

    else:
        print("请求失败")
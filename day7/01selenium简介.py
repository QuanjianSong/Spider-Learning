'''
selenium模块的基本使用
    便携的获取网站中的动态加载数据
    便携实现模拟登录
什么恶事selenium模块？
    基于浏览器自动化的一个模块。让爬虫模拟人对浏览器的操作

selenium的安装流程：
    - 环境安装 pip install selenium
    - 下载一个浏览器的驱动程序
        google下载路径: https://googlechromelabs.github.io/chrome-for-testing/
        edge下载路径: https://blog.csdn.net/m0_61552056/article/details/134956649
    - 实例化一个浏览器对象
    - 编写浏览器自动化代码
'''
import time
from selenium import webdriver
from lxml import etree


if __name__ == '__main__':
    # 实例化浏览器对象（一定要传入驱动程序）
    path = '/Users/QuanjianSong/Desktop/my_projects/Spider/day7/chromedriver-mac-arm64/chromedriver'
    browser = webdriver.Chrome(executable_path=path)
    # 让浏览器发起一个url请求
    browser.get("https://www.bilibili.com/")
    # time.sleep(5)

    # 获取页面源码数据
    page_text = browser.page_source

    with open("./page.html", 'w') as fp:
        fp.write(page_text)

    tree = etree.HTML(page_text)
    # print(page_text)
    video_src = tree.xpath('''/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/div[1]/a[7]/text()''')
    print(video_src)

    # 浏览器怎么关闭？
    time.sleep(5)
    browser.quit()
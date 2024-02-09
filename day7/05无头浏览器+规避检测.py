'''
无头浏览器，无可视化界面

'''
from selenium import webdriver
# 实现无可视化界面
from selenium.webdriver.chrome.options import Options
# 实现规避检测
from selenium.webdriver import ChromeOptions
import time
from lxml import etree


if __name__ == '__main__':
    driver_path = '/Users/QuanjianSong/Desktop/my_projects/Spider/day7/chromedriver-mac-arm64/chromedriver'
    # 设置无头对象参数
    chrone_options = Options()
    chrone_options.add_argument('--headless')
    chrone_options.add_argument('--disable-gpu')
    # 设置规避检测参数
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 设置无头对象, 如何规避被检测风险？
    browers = webdriver.Chrome(executable_path=driver_path, chrome_options=chrone_options, options=option)

    # 发起请求
    url = 'https://www.baidu.com'
    browers.get(url)
    print(browers.page_source)


    browers.quit()
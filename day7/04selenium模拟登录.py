'''
模拟登录qq空间

'''
import time
from selenium import webdriver

if __name__ == '__main__':
    driver_path = '/Users/QuanjianSong/Desktop/my_projects/Spider/day7/chromedriver-mac-arm64/chromedriver'
    browers = webdriver.Chrome(executable_path=driver_path)

    url = 'https://qzone.qq.com/'
    browers.get(url)
    # 切换iframe
    browers.switch_to.frame('login_frame')

    # 定位登录标签
    button_login = browers.find_element_by_id('switcher_plogin')
    button_login.click() # 点击账号密码登录

    # 定位账号密码
    username_tag = browers.find_element_by_id('u')
    password_tag = browers.find_element_by_id('p')

    # 输入账号密码
    username_tag.send_keys('')
    time.sleep(1)
    password_tag.send_keys('')
    time.sleep(1)

    # 点击登录按钮
    login = browers.find_element_by_id('login_button')
    login.click()
    
    time.sleep(20)

    # 退出！
    browers.quit()

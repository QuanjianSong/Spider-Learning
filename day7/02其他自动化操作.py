'''
以淘宝举例, 自动化代码
    发起请求：get（url）
    标签定位：find_element系列的方法
    标签交互：send_keys（‘xxx）
    按钮点击：.click()
    截图：.save_screenshot()
    根据给定的坐标进行点击操作 
    执行js程序：excute_script('jsconde)
    前进、后退：forward（）、back（）
    关闭浏览器：quit（）
    
'''

from selenium import webdriver
import time
from PIL import Image
from selenium.webdriver import ActionChains # 导入动作链的类


if __name__ == '__main__':
    # 实例化浏览器对象（一定要传入驱动程序）
    path = '/Users/QuanjianSong/Desktop/my_projects/Spider/day7/chromedriver-mac-arm64/chromedriver'
    browser = webdriver.Chrome(executable_path=path)
    # 让浏览器发起一个url请求, 对淘宝
    browser.get("https://www.taobao.com/")

    time.sleep(5)
    # 标签定位，找到搜索栏
    search_input = browser.find_element_by_class_name("rax-textinput")

    # 标签交互, 向搜索框中传递一个值，模拟用户的搜索操作。
    search_input.send_keys("美食")

    # # 标签定位，找到搜索按钮, 二选一都可以。
    search_button = browser.find_element_by_class_name("search-button-text")
    # search_button = browser.find_element_by_css_selector(".btn-search")
    
    # 如何滑动窗口？---》 执行js代码
    command = 'window.scrollTo(0, document.body.scrollHeight)'
    browser.execute_script(command)
    time.sleep(2)

    # 点击搜索按钮
    search_button.click()

    # 访问另外一个界面
    browser.get("https://www.baidu.com/")
    time.sleep(2)

    # 对浏览器截图
    browser.save_screenshot('./tmp.jpg')

    # 坐标裁剪
    # code_img_ele = browser.find_element_by_xpath("...")
    # location = code_img_ele.location # 获得code_img_ele的左上角的坐标
    # size = code_img_ele.size # 获得对应的高宽
    # img = Image.open("./tmp.jpg")
    # angle = (0, 0, 250, 250)
    # frame = img.crop(angle)
    # frame.save('./result.jpg')

    # 根据给定的坐标进行点击操作
    # position = (256, 256)
    # action = ActionChains(browser)
    # # 以一个element为基准进行偏移，而不是全局的偏移
    # # 全局的偏移为move_by_offsets
    # action.move_to_element_with_offset(code_img_ele, position[0], position[1]).click().perform()()
    # time.sleep(2)
    
    # 让浏览器回退 
    browser.back()
    time.sleep(2)

    # 让浏览器前进
    browser.forward()
    
    # 切换界面


    time.sleep(5)
    browser.quit()
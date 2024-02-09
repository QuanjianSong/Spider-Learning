'''
想要定位的标签存在于iframe之中，则必须通过如下的操作再进行标签定位。
'''
from selenium import webdriver
import time
from selenium.webdriver import ActionChains # 导入动作链的类


if __name__ == '__main__':
    driver_path = '/Users/QuanjianSong/Desktop/my_projects/Spider/day7/chromedriver-mac-arm64/chromedriver'
    browers = webdriver.Chrome(executable_path=driver_path)

    # 定位网站
    browers.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")

    # 想要定位的标签存在于iframe之中，则必须通过如下的操作再进行标签定位。
    browers.switch_to.frame('iframeResult') # 切换浏览器标签定位的作用域
    # 标签定位
    div = browers.find_element_by_id("draggable")

    # --------------滑动滑块，执行一系列动作链-----------------
    # 绑定动作链
    action = ActionChains(browers)
    # 点击长按指定的标签
    action.click_and_hold(div)
    # 循环，每次移动一点
    for i in range(5):
        # .move_by_offset（x， y）
        action.move_by_offset(17, 0).perform() # .proform表示立即执行
        time.sleep(0.3)
    # 释放动作链
    action.release()

    time.sleep(2)
    # 浏览器退出
    browers.quit()

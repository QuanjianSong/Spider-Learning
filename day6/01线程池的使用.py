import requests
import time
from lxml import etree
from multiprocessing.dummy import Pool

# 使用单线程
def get_page(url):
    print("正在下载：", url)
    time.sleep(2)
    print("下载成功：", url)
    return url

# 基于线程池的方式

if __name__ == '__main__':
    name_list = ['xiaozi', 'aa', 'cc', 'bb']
    start_time = time.time()

    # for i in range(len(name_list)):
    #     get_page((name_list[i]))

    # 实例化一个线程池对象
    pool = Pool(16) # 四个线程
    # 将name_list中每个列表元素传递给get_page
    result = pool.map(get_page, name_list)
    
    end_time = time.time()
    print(f"{end_time - start_time} second")

    print(result)
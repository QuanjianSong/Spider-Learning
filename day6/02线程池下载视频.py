'''
需求：爬取梨视频的视频数据
原则：线程池处理的是阻塞且耗时的操作, 而不是其他操作。
'''
import requests
from lxml import etree
from multiprocessing.dummy import Pool


if __name__ == '__main__':
    # url = 'https://www.pearvideo.com/category_5'
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    # }
    # session = requests.Session()
    # page_text = session.get(url=url, headers=headers).text

    # tree = etree.HTML(page_text)
    # li_list = tree.xpath('/html/body/div[2]/ul')
    # for li in li_list[1]:
    #     detailed_url = 'https://www.pearvideo.com/' + li.xpath('./li/a/@href')[0]
    #     name = li.xpath('./li/a/div[2]/text()')[0]
    #     # 解析地址
    #     video_page = session.get(detailed_url, headers=headers).text
    #     tree = etree.HTML(video_page)
    #     video_url = etree.xpath('/html/body/div[2]/div[1]/div[1]/div[1]/div[1]/div/video')

    # pool = Pool(4)
    # pool.close()
    # pool.join()

    url = 'https://video.pearvideo.com/mp4/adshort/20210818/cont-1739298-15749522_adpkg-ad_hd.mp4'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    session = requests.Session()
    video_content = session.get(url=url, headers=headers).content
    with open('./video.mp4', 'wb') as fp:
        fp.write(video_content)

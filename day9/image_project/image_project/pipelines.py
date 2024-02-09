# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline


# 需要继承ImagesPipeline，重写三个方法
class ImageProjectPipeline(ImagesPipeline):
    # 就是可以根据图片地址进行数据请求
    def get_media_requests(self, item, info):
        print(item)
        yield scrapy.Request(item['src'])

    # 指定图片存储的路径
    def file_path(self, request, response=None, info=None):
        img_name = request.url.split('/')[-1]
        print(img_name)
        return img_name
    
    def item_completed(self, results, item, info):
        return item # 返回下一个即将执行的pipeline
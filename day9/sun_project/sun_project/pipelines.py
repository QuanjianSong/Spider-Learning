# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SunProjectPipeline:
    def process_item(self, item, spider):
        # 写入数据库时，如何保证数据的一致性？？？ ---> 根据唯一索引id，做插入。
        if item.__class__.__name__ == 'SunProjectDetailedItem':
            print('content:{}'.format(item['content']))
        else:
            print('nums'.format(item['nums']))
            print('title'.format(item['title']))
        return item

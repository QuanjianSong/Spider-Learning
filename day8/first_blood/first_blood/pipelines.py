# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


# 管道文件中，一个管道类表示将一组数据存储到一个平台
class FirstBloodPipeline:
    fp = None
    # 重写父类的一个方法：该方法只在开始爬虫的时候被调用一次
    # 自动调用，不用显示调用
    def open_spider(self, spider):
        print("开始爬虫.......")
        self.fp = open("./test.txt", 'w', encoding='utf-8')
    
    # 重写父类的一个方法，只在结束调用一次
    # 自动调用，同样不用显示调用
    def close_spider(self, spider):
        print("结束爬虫！")
        self.fp.close()

    # 专门处理item类型的数据
    # 该方法可以接受爬虫文件提交过来的item对象
    # 该方法每接受懂啊一个item就会被调用一次
    def process_item(self, item, spider):
        title = item['title']
        conten_src = item['conten_src']

        # 写到文件流中
        self.fp.write(title+ ', ' + conten_src + '\n')

        return item # 就会传递给下一个即将被执行的管道类

class MysqlPipeline:
    conn = None
    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test', charset='utf8')

    def process_item(self, item, spider):
        # 获得游标
        self.cursor = self.conn.cursor()
        # item内容的获取
        title = item['title']
        conten_src = item['conten_src']
        try:
            self.cursor.execute("insert into article(title, content) values(%s, %s)", (title, conten_src))
        except Exception as e:
            print(e)
            # 回滚
            self.conn.rollback()
        
        return item # 就会传递给下一个即将被执行的管道类
    
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

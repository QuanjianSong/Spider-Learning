import scrapy
from ..items import FirstBloodItem


class FirstSpider(scrapy.Spider):
    # 名称，唯一标识
    name = "first"
    # 在start_urls中允许的url，一般可以注释掉。
    # allowed_domains = ["www.xxx.com"]
    # 要访问的urls
    start_urls = ["https://m.shicimingju.com/book/sanguoyanyi.html"]

    # def parse(self, response):
    #     # 解析标题+段子 # 这里不用etree对象了, 直接调用xpath
    #     div_list = response.xpath("/html/body/div[3]/div/div[3]/ul/li") 
    #     # print(div_list)
    #     all_data = []
    #     for div in div_list:
    #         # xpath 返回的是列表，但是列表元素一定是selector元素
    #         # 与普通的xpath不一样的是，需要用.extract提取出来
    #         title = div.xpath("./a/text()")[0].extract()
    #         # 列表也能直接调用，返回的也是一个列表。
    #         conten_src = div.xpath("./a/@href").extract()[0]
    #         # print(title)
    #         # print(conten_src)
    #         dic = {
    #             'title': title,
    #             'conten_src': conten_src
    #         }
    #         all_data.append(dic)
    #     # with open('test.jsonl', 'w') as fp:
    #     #     fp.write(str(all_data))

    #     return all_data

    def parse(self, response):
        # 解析标题+段子 # 这里不用etree对象了, 直接调用xpath
        div_list = response.xpath("/html/body/div[3]/div/div[3]/ul/li") 
        # print(div_list)
        for div in div_list:
            # xpath 返回的是列表，但是列表元素一定是selector元素
            # 与普通的xpath不一样的是，需要用.extract提取出来
            title = div.xpath("./a/text()")[0].extract()
            # 列表也能直接调用，返回的也是一个列表。
            conten_src = div.xpath("./a/@href").extract()[0]
            
            # 将要保存的信息封装到item中。
            item = FirstBloodItem()
            # 用字典的方式去访问
            item['title'] = title
            item['conten_src'] = conten_src

            # 将item提交给管道
            yield item



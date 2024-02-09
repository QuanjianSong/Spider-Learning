import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import SunProjectItem, SunProjectDetailedItem


class SunSpider(CrawlSpider):
    name = "sun"
    # allowed_domains = ["www.xxx.com"]

    start_urls = ["https://wz.sun0769.com/political/index/supervise?page=5"]

    # 链接提取器，根据指定规则进行指定链接的提取，allow=正则表达式
    link = LinkExtractor(allow=r"page=\d+")
    link_detailed = LinkExtractor(allow=r"/political/politics/index\?id=\d+")
    # https://wz.sun0769.com/political/politics/index?id=680297
    
    # 规则解析器, 用来解析规则提取器提取对应的链接，解析函数为parse_item
    rules = ( # 顺序执行，递归遍历
        # 如何爬取全站？这里的follow改成true即可。可以链接提取器继续作用到链接提取器的link 
        Rule(link, callback="parse_item", follow=True), # follow是什么意思？
        Rule(link_detailed, callback="parse_detailed", follow=False),
    )

    # 这个parse_item就是之前的parse的方法，一样的类比。
    def parse_item(self, response):
        li_list = response.xpath("/html/body/div[2]/div[3]/ul/li")
        for li in li_list:
            nums = li.xpath("./span[1]/text()").extract_first()
            title = li.xpath("./span[3]//text()").extract_first()
            # print(nums, title)
            item = SunProjectItem(nums=nums, title=title)   

        # 如果爬取的信息不在一个界面中怎么办？ ---> 再指定一个链接提取器以及规则解析器
        yield item

    # 无法实现请求传参，因此可以将两个parse存到两个item中，丢给一个pipeline
    def parse_detailed(self, response):
        content = response.xpath("/html/body/div[1]/div[3]//text()").extract()
        content = ''.join(content).strip()

        item = SunProjectDetailedItem(content=content)

        yield item
        


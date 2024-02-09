import scrapy
from selenium import webdriver
from ..items import WangyiProjectItem


class WangyiSpider(scrapy.Spider):
    name = "wangyi"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://news.163.com/"]

    module_urls = []
    # 解析五大板块对应的url
    def __init__(self):
        path = '/Users/QuanjianSong/Desktop/my_projects/Spider/day7/chromedriver-mac-arm64/chromedriver'
        self.browser = webdriver.Chrome(executable_path=path)

    def parse(self, response):
        li_list = response.xpath("/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div/ul/li")
        index_list = [1, 2, 3, 4, 5]
        for index in index_list:
            module_url = li_list[index].xpath('./a/@href').extract_first()
            self.module_urls.append(module_url)
        
        print(self.module_urls)

        # 依此对每一个模块下的页面进行请求
        for url in self.module_urls:
            yield scrapy.Request(url=url, callback=self.parse_module)
        
    # 解析每一个板块页面中对应新闻的标题和新闻详情页的url。
    # 每个板块都是动态加载出来的。
    def parse_module(self, response):
        div_list = response.xpath("/html/body/div[1]/div[3]/div[3]/div[1]/div[1]/div/ul/li/div/div")
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            new_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()
                    
            # print(title)
            # print(new_detail_url)

            item = WangyiProjectItem()
            item['title'] = title

            # 对新闻详情页的url发起请求, 这个不是动态加载数据，可以用普通的解析parse_detail
            if new_detail_url is not None:
                # print(new_detail_url)
                yield scrapy.Request(url=new_detail_url, callback=self.parse_detail, meta={'item': item})

    
    # 对新闻页的详细请求。
    def parse_detail(self, response):
        content = response.xpath('/html/body/main//text()').extract()
        content = ''.join(content)

        item = response.meta['item']
        print(item)
        item['content'] = content

        # 提交管道进行持久化存储
        yield item

    def closed(self, spider):
        self.browser.quit()

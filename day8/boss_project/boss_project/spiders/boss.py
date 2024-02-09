import scrapy
from ..items import BossProjectItem

class BossSpider(scrapy.Spider):
    name = "boss"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.zhipin.com/job_detail/"]
    # start_urls = ["https://www.baidu.com/"]

    # 回调函数接受item
    def parse_details(self, response):
        # 通过这样的方式接受参数
        item = response.meta['item']
        job_desc = response.xpath("/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]//text()").extract()
        job_desc = ''.join(job_desc)
        
        item['job_desc'] = job_desc
        print(job_desc)

        yield item

    def parse(self, response):
        print(response)
        li_list = response.xpath('//*[@id="main"]/div/div[3]/ul/li')
        print(111)
        print(li_list)
        for li in li_list:
            item = BossProjectItem()
            job_name = li.xpath('''.//div[@class="info-primary"]/h3/a/div[1]/text()''').extract_first()
            print(job_name)
            item['job_name'] = job_name
            detail_url = 'https://www.zhipin.com' + li.xpath('''.//div[@class="info-primary"]/h3/a/@href''')
            
            # 对详情页发请求获取详情页的页面源码数据,
            # 这里需要额外传参数，用meta的参数,值为字典。
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item})
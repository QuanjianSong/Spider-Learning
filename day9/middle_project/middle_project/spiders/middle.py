import scrapy


class MiddleSpider(scrapy.Spider):
    # 爬取百度
    name = "middle"
    # allowed_domains = ["www.xxx.com"]
    # start_urls = ["https://www.baidu.com"]
    start_urls = ["https://www.youtube.com/"]

    def parse(self, response):
        page_text = response.text

        with open('ip.html', 'w', encoding='utf-8') as fp:
            fp.write(page_text)

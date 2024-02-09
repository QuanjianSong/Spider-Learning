import scrapy


class FirstSpider(scrapy.Spider):
    name = "first"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["http://www.521609.com/meinvxiaohua/"]

    # 生成一个通用的url模版
    url = "http://www.521609.com/meinvxiaohua/list12%d.html"
    page_num = 2

    def parse(self, response):
        li_list = response.xpath("//div[@class='crawler']")
        for li in list(li_list):
            # 可以用｜做多选
            img_name = li.xpath("//img[@class=123] | //img").extract_first()
            print(img_name)

        if self.page_num <= 11:
            self.page_num += 1
            new_url = format(self.url%self.page_num)
            # 手动请求发送, call_back回调函数专门用于数据解析
            # 这里是递归调用
            yield scrapy.Request(url=new_url, callback=self.parse)


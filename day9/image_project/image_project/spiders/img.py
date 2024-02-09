import scrapy
from ..items import ImageProjectItem


class ImgSpider(scrapy.Spider):
    name = "img"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://sc.chinaz.com/tupian/"]

    def parse(self, response):
        div_list = response.xpath("/html/body/div[3]/div[2]/div")
        # 为什么解析到的图片为空? 图片懒加载！
        # print(div_list)
        for div in div_list:
            # 这里地址要改变，使用伪属性，不能让他懒加载
            src_path = 'https:' + div.xpath("./img/@data-original").extract_first()
            print(src_path)
            # 构造item
            item = ImageProjectItem()
            item['src'] = src_path

            yield item

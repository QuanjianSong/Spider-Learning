# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunProjectItem(scrapy.Item):
    nums = scrapy.Field()
    title = scrapy.Field()


class SunProjectDetailedItem(scrapy.Item):
    content = scrapy.Field()

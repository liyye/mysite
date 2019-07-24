# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhillItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    q1 = scrapy.Field()  # 实现了 __get__  __set__  __delete__
    q2 = scrapy.Field()
    q3 = scrapy.Field()
    q4 = scrapy.Field()
    q5 = scrapy.Field()
    q6 = scrapy.Field()
    q7 = scrapy.Field()
    q8 = scrapy.Field()
    q9 = scrapy.Field()



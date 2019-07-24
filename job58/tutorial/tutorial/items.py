# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job1 = scrapy.Field()  # 实现了 __get__  __set__  __delete__
    job11 = scrapy.Field()
    job2 = scrapy.Field()
    job3 = scrapy.Field()
    job4 = scrapy.Field()
    job5 = scrapy.Field()


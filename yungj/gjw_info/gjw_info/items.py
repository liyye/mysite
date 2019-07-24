# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GjwInfoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    sex = scrapy.Field()
    age = scrapy.Field()
    addr = scrapy.Field()
    job = scrapy.Field()
    salary = scrapy.Field()
    edu = scrapy.Field()




# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GanjiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    sex = scrapy.Field()
    age = scrapy.Field()
    edu = scrapy.Field()
    addr = scrapy.Field()
    excjob = scrapy.Field()
    excsalary = scrapy.Field()

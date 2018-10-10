# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class QianchengwuyouItem(scrapy.Item):
    # define the fields for your item here like:
    jobPosition = scrapy.Field()
    jobCompany = scrapy.Field()
    jobArea = scrapy.Field()
    jobSale = scrapy.Field()
    jobDate = scrapy.Field()
    pass

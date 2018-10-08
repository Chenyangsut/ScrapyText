# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# from scrapy import Item,Field
#
#
# class QianchengwuyouItem(Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     name = Field()  # 公司名称
#     duty = Field()  # 工作的标题
#     location = Field()  # 公司地址
#     sallary = Field()  # 薪水
#     time = Field()  # 时间
import scrapy


class QianchengwuyouItem(scrapy.Item):
    # define the fields for your item here like:
    jobPosition = scrapy.Field()
    jobCompany = scrapy.Field()
    jobArea = scrapy.Field()
    jobSale = scrapy.Field()
    jobDate = scrapy.Field()
    pass

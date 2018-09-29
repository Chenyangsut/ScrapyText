# -*- coding: utf-8 -*-
import scrapy
import re
from zhengdao.items import ZhengdaoItem
from scrapy.http import Request
from scrapy.spider import CrawlSpider
from scrapy.selector import Selector

class QianlongSpider(CrawlSpider):
    name = 'qianlong'
    allowed_domains = ['biquta.com']
    start_urls = [
        'https://www.biquta.com/1_1733/'
    ]  # 正道潜龙目录列表

    #  获取书的章节URL
    def parse(self, response):
        chapter_urls = response.xpath(
            '//div[@id="list"]/dl/dd/a[@style=""]/@href').extract()
        for chapter_url in chapter_urls:
            yield Request('https://www.biquta.com'+chapter_url,callback=self.parse_content)


    # 获取小说名字,章节的名字和内容
    def parse_content(self, response):
        # 小说名字

        name = response.xpath(
            u'//div[@class="con_top"]/a[@title="正道潜龙"]/text()').extract_first()

        result = response.text
        # 小说章节名字
        chapter_name = response.xpath(
            '//div[@class="bookname"]/h1/text()').extract_first()
        # 小说章节内容
        chapter_content_reg = r'<div id="content">.*?<script>'
        chapter_content_1 = re.findall(chapter_content_reg, result,flags=re.S)[0]
        chapter_content = chapter_content_1.replace('<br/>', '')

        item = ZhengdaoItem()
        item['name'] = name
        item['chapter_name'] = chapter_name
        item['chapter_content'] = chapter_content
        yield item

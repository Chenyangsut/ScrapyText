# -*- coding: utf-8 -*-
# import scrapy
# import os
# from renren.items import RenrenItem
# from scrapy.http import Request,FormRequest
# from scrapy.spider import CrawlSpider
#
# class RrloginSpider(CrawlSpider):
#     name = 'rrlogin'
#     allowed_domains = ['renren.com']
#     start_urls = ['http://zhibo.renren.com/top']
#     headers ={
#         "Accept":"*/*",
#         "Accept-Encoding": "gzip, deflate",
#         "Accept-Language": "zh-CN,zh;q=0.9",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
#         "X-Requested-With": "XMLHttpRequest"
#     }
#     mydata = {
#         'email':'18802404422',
#         'icode':'',
#         'origURL':'http://www.renren.com/home',
#         'domain':'renren.com',
#         'key_id':'1',
#         'captcha_type':'web_login',
#         'password':'1dc9b7665ee1b94f41b63fa2f81ab86a9b1b3e4a280b2002dc7eca77b36c68e5',
#         'rkey':'d4e7485a436e32e5d3f7b0af6ddbe52b',
#         'f':'http%3A%2F%2Fzhibo.renren.com%2Ftop'
#     }
#     def start_requests(self):
#         return[FormRequest(url='http://renren.com/SysHome.do',headers=self.headers,method='post',formdata=self.mydata,dont_filter=True,callback=self.parse_login)]
#
#     def parse_login(self,response):
#         return scrapy.Request('http://zhibo.renren.com/top',dont_filter=True,callback=parse)
#
#     def parse(self, response):
#         title = response.xpath('//div[@class="hd-main"]/h1[@class="hd-logo"]/a/text()').extract_first()
#         item = RenrenItem()
#         item['title'] = item
#         with open('F:/text/111/1.txt', 'w',encoding='utf-8') as f:
#             f.write('成功')
#         return item

import scrapy
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class RrloginSpider(scrapy.Spider):
    name = 'rrlogin'
    allowed_domains = ["'renren.com'"]
    start_urls = ['http://www.renren.com/']
    url = 'http://www.renren.com/'

    def start_requests(self):
        base_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp='
        s = time.strftime("%S")
        ms = int(round(time.time() % (int(time.time())), 3) * 1000)
        date_time = '20188010' + str(s) + str(ms)
        login_url = base_url + date_time
        data = {
            'email':'18802404422',
            'icode':'',
            'origURL':'http://www.renren.com/home',
            'domain':'renren.com',
            'key_id':'1',
            'captcha_type':'web_login',
            'password':'1dc9b7665ee1b94f41b63fa2f81ab86a9b1b3e4a280b2002dc7eca77b36c68e5',
            'rkey':'d4e7485a436e32e5d3f7b0af6ddbe52b',
            'f':'http%3A%2F%2Fzhibo.renren.com%2Ftop'
        }
        yield scrapy.FormRequest(url=login_url, formdata=data,
                                 callback=self.parse_login, dont_filter=True)

    def parse_login(self, response):
        yield scrapy.Request(url='http://www.renren.com/880151247/profile',
                             callback=self.parse_text, dont_filter=True)

    def parse_text(self, response):
        with open(r'F:\text\111\大鹏.html'.decode('utf-8'), 'w') as f:
            f.write(response.text)





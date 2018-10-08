# -*- coding: utf-8 -*-
# import re
# import scrapy
# from qianchengwuyou.items import QianchengwuyouItem
# from scrapy.http import Request
# from scrapy.spider import CrawlSpider
#
# class WuyaoSpider(CrawlSpider):
#     name = 'wuyao'
#     allowed_domains = ['51job.com']
#     start_urls = ['https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']
#
#     def parse(self, response):
#         chapter_urls = response.xpath(
#             '//div[@class="el"]/p[@class="t1"]/span/a[@target="_blank"]/@href').extract()
#         for chapter_url in chapter_urls:
#             yield Request(chapter_url,callback=self.parse_content)
#
#     def parse_content(self,response):
#         job = response.xpath('//div[@class="cn"]/h1/text()').extract_first()
#         wages = response.xpath('//div[@class="cn"]/strong/text()').extract_first()
#         company = response.xpath('//div[@class="cn"]/p[@class="cname"]/a[@class="catn"]/text()').extract_first()
#         result = response.text
#         content_reg = r'<div class="bmsg job_msg inbox">.*?<div class="mt10">'
#         content1 = re.findall(content_reg,result,re.S)[0]
#         content2 = content1.replace('<p>','')
#         content = content2.replace('</p>','\n')
#
#         item = QianchengwuyouItem()
#         item['job'] = job
#         item['wages'] = wages
#         item['company'] = company
#         item['content'] = content
#         yield item
# -*- coding: utf-8 -*-
# import scrapy
# from scrapy.spiders import CrawlSpider,Rule
# from scrapy.linkextractors import LinkExtractor
# from qianchengwuyou.items import QianchengwuyouItem
# class WuyaoSpider(CrawlSpider):
#     name = "wuyao"
#     #这里爬取两个网站，一个是php工程师，一个是python工  程师
#     start_urls=["https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="]
#     rules={
#         Rule(LinkExtractor(allow="http:\/\/search.51job.com\/list\/",restrict_xpaths="//div[@class='p_in']"),callback="self.paser_item",follow=True),
#         # Rule(LinkExtractor(allow=""))
#     }
#
#     def paser_item(self,response):
#         divs=response.xpath("//div[@class='el']")
#         item=QianchengwuyouItem()
#
#         for div in divs:
#             try:
#                 item['duty'] = div.xpath("./p/span/a/text()")[0].extract().strip()
#                 item['time'] = div.xpath("./span[4]/text()").extract()
#                 item['name'] = div.xpath("./span[1]/a/text()").extract()
#                 item['location'] = div.xpath("./span[2]/text()").extract()
#                 item['sallary'] = div.xpath("./span[3]/text()").extract()
#                 yield item
#             except Exception:
#                 pass
import scrapy
from ..items import QianchengwuyouItem

class WuyaoSpider(scrapy.Spider):
    name = 'wuyao'
    #allowed_domains = ['search.51job.com/list/010000,000000,0000,00,9,99,%2520,2,1.html']
    #start_urls = ['https://search.51job.com/list/010000,000000,0000,00,9,99,%2520,2,1.html/']
    start_urls = [
        'https://search.51job.com/list/010000,000000,0000,01,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def parse(self, response):
        currentPageItems = response.xpath('/html/body/div[@class="dw_wp"]/div[@class="dw_table"]/div[@class="el"]')
        print(currentPageItems)

        # currentPageItems = response.xpath('//div[@class="el"]')
        for jobItem in currentPageItems:
            print('----',jobItem)
            jobspidersItem = QianchengwuyouItem()

            jobPosition = jobItem.xpath('p[@class="t1 "]/span/a/text()').extract()
            if jobPosition:
                #print(jobPosition[0].strip())
                jobspidersItem['jobPosition'] = jobPosition[0].strip()

            jobCompany = jobItem.xpath('span[@class="t2"]/a/text()').extract()
            if jobCompany:
                #print(jobCompany[0].strip())
                jobspidersItem['jobCompany'] = jobCompany[0].strip()

            jobArea = jobItem.xpath('span[@class="t3"]/text()').extract()
            if jobArea:
                #print(jobArea[0].strip())
                jobspidersItem['jobArea'] = jobArea[0].strip()

            jobSale = jobItem.xpath('span[@class="t4"]/text()').extract()
            if jobSale:
                # print(jobCompany[0].strip())
                jobspidersItem['jobSale'] = jobSale[0].strip()

            jobDate = jobItem.xpath('span[@class="t5"]/text()').extract()
            if jobDate:
                # print(jobCompany[0].strip())
                jobspidersItem['jobDate'] = jobDate[0].strip()



            yield jobspidersItem  # 通过yield 调用输出管道
            pass
        nextPageURL = response.xpath('//li[@class="bk"]/a/@href').extract()  # 取下一页的地址
        print(nextPageURL)
        if nextPageURL:
            url = response.urljoin(nextPageURL[-1])
            print('url', url)
            # 发送下一页请求并调用parse()函数继续解析
            yield scrapy.Request(url, self.parse, dont_filter=False)
            pass
        else:
            print("退出")
        pass
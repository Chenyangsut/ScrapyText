# -*- coding: utf-8 -*-

import scrapy
from ..items import QianchengwuyouItem

class WuyaoSpider(scrapy.Spider):
    name = 'wuyao'
    #allowed_domains = ['search.51job.com/list/010000,000000,0000,00,9,99,%2520,2,1.html']
    #北京python搜索结果
    start_urls = [
        'https://search.51job.com/list/080200%252C070200%252C090200%252C060000%252C030800,000000,0000,01,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def parse(self, response):
        #页面需要结果
        currentPageItems = response.xpath('/html/body/div[@class="dw_wp"]/div[@class="dw_table"]/div[@class="el"]')
        print(currentPageItems)

        for jobItem in currentPageItems:
            print('----',jobItem)
            jobspidersItem = QianchengwuyouItem()

            #工作岗位
            jobPosition = jobItem.xpath('p/span/a/text()').extract()
            if jobPosition:
                # print(jobPosition[0].strip())
                jobspidersItem['jobPosition'] = jobPosition[0].strip()
                # print(type(jobspidersItem['jobPosition']))

            #公司名
            jobCompany = jobItem.xpath('span[@class="t2"]/a/text()').extract()
            if jobCompany:
                # print(jobCompany[0].strip())
                jobspidersItem['jobCompany'] = jobCompany[0].strip()
                # print(type(jobspidersItem['jobCompany']))


            #公司地址
            jobArea = jobItem.xpath('span[@class="t3"]/text()').extract()
            if jobArea:
                #print(jobArea[0].strip())
                jobspidersItem['jobArea'] = jobArea[0].strip()


            #薪资
            jobSale = jobItem.xpath('span[@class="t4"]/text()').extract()
            if jobSale:
                # print(jobCompany[0].strip())
                jobspidersItem['jobSale'] = jobSale[0].strip()


            #发布日期
            jobDate = jobItem.xpath('span[@class="t5"]/text()').extract()
            if jobDate:
                # print(jobDate[0].strip())
                jobspidersItem['jobDate'] = jobDate[0].strip()
                # print(type(jobspidersItem['jobDate']))



            yield jobspidersItem  # 通过yield 调用输出管道
            pass

        #下一页
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
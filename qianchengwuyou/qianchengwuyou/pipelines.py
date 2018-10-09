# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import os
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
import pymysql
from scrapy import log
import codecs
import pymysql.cursors
from twisted.enterprise import adbapi
class QianchengwuyouPipeline(object):

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            port=settings['MYSQL_PORT'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('pymysql', **dbargs)
        return cls(dbpool)

    def __init__(self,dbpool):
        self.dbpool = dbpool

    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self._conditional_insert, item,
                                       spider)  # 调用插入的方法
        log.msg("-------------------连接好了-------------------")
        d.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        d.addBoth(lambda _: item)
        return d

    def _conditional_insert(self, conn, item, spider):
        log.msg("-------------------打印-------------------")
        conn.execute(
            "insert into beijing(jobcompany, jobarea, jobsale) values(%s, %s, %s)",
            (item["jobCompany"], item["jobArea"],
             item["jobSale"]))
        # conn.execute("insert into shili(jobPosition, jobCompany, jobArea, jobSale) values(%s, %s, %s，%s)",(str(item["jobPosition"]),item["jobCompany"], item["jobArea"], item["jobSale"]))
        log.msg("-------------------一轮循环完毕-------------------")

    def _handle_error(self, failue, item, spider):
        print(failue)


    # def process_item(self, item, spider):
    #     # jobPosition = item["jobPosition"][0]
    #     jobCompany = item["jobCompany"][0]
    #     jobArea = item["jobArea"][0]
    #     jobSale = item["jobSale"][0]
    #     jobDate = item["jobDate"][0]
    #     sql = "insert into shili values('unknow','{jobCompany}','{jobArea}','{jobSale}','{jobDate)}')"
    #     self.conn.query(sql)
    #     return item
    # def close_spider(self,spider):
    #     self.conn.close()




        # curpath = 'f:/job/'
        # file_name = str(item['jobCompany'])+str(item['jobPosition']) + '.txt'
        # file_path = curpath + file_name.decode('utf-8')
        # fp = open(file_path, 'w')
        # fp.write(item['jobPosition'] + item['jobCompany'] + item['jobArea'] + item['jobSale'] + item['jobDate'] + '\n')
        # fp.close()
        # if os.path.exists(file_path):
        #     pass
        # else:
        #     fp = open(file_path,'w')
        #     fp.write(
        #         item['jobPosition'] + item['jobCompany'] + item['jobArea'] +
        #         item['jobSale'] + item['jobDate'] + '\n')
        #     fp.close()
        # pass

    # def process_item(self, item, spider):
    #     print('职位:', item['jobPosition'])
    #     print('公司:', item['jobCompany'])
    #     print('工作地点:', item['jobArea'])
    #     print('薪资:', item['jobSale'])
    #     print('发布时间:', item['jobDate'])
    #     print('----------------------------')
    #     return item
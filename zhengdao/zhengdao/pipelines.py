# -*- coding: utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pymysql
from scrapy import log
import codecs
import pymysql.cursors
from twisted.enterprise import adbapi

class ZhengdaoPipeline(object):
    # @classmethod
    # def from_settings(cls, settings):
    #     dbargs = dict(
    #         host=settings['MYSQL_HOST'],
    #         db=settings['MYSQL_DBNAME'],
    #         user=settings['MYSQL_USER'],
    #         passwd=settings['MYSQL_PASSWD'],
    #         port=settings['MYSQL_PORT'],
    #         charset='utf8',
    #         cursorclass=pymysql.cursors.DictCursor,
    #         use_unicode=True,
    #     )
    #     dbpool = adbapi.ConnectionPool('pymysql', **dbargs)
    #     return cls(dbpool)
    #
    # def __init__(self,dbpool):
    #     self.dbpool = dbpool
    #
    # def process_item(self, item, spider):
    #     d = self.dbpool.runInteraction(self._conditional_insert, item,
    #                                    spider)  # 调用插入的方法
    #     log.msg("-------------------连接好了-------------------")
    #     d.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
    #     d.addBoth(lambda _: item)
    #     return d
    #
    # def _conditional_insert(self, conn, item, spider):
    #     log.msg("-------------------打印-------------------")
    #
    #     conn.execute(
    #         "insert into zhengdao(title) values(%s)",
    #         item['chapter_name'])
    #     log.msg("-------------------一轮循环完毕-------------------")
    #
    # def _handle_error(self, failue, item, spider):
    #     print(failue)




    def process_item(self, item, spider):

        # 小说存放路径
        curPath = 'f:/text/'
        file_name = str(item['chapter_name']) + '.txt'
        file_path = curPath + '/' + file_name.decode('utf-8')
        # 写入内容
        if os.path.exists(file_path):
            pass
        else:
            fp = open(file_path,'w')
            fp.write(item['chapter_content'] + '\n')
            fp.close()
        pass

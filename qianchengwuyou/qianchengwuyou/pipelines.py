# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class QianchengwuyouPipeline(object):
    def process_item(self, item, spider):
        curpath = 'f:/job/'
        file_name = str(item['jobCompany'])+str(item['jobPosition']) + '.txt'
        file_path = curpath + file_name.decode('utf-8')
        # fp = open(file_path, 'w')
        # fp.write(item['jobPosition'] + item['jobCompany'] + item['jobArea'] + item['jobSale'] + item['jobDate'] + '\n')
        # fp.close()
        if os.path.exists(file_path):
            pass
        else:
            fp = open(file_path,'w')
            fp.write(
                item['jobPosition'] + item['jobCompany'] + item['jobArea'] +
                item['jobSale'] + item['jobDate'] + '\n')
            fp.close()
        pass

    # def process_item(self, item, spider):
    #     print('职位:', item['jobPosition'])
    #     print('公司:', item['jobCompany'])
    #     print('工作地点:', item['jobArea'])
    #     print('薪资:', item['jobSale'])
    #     print('发布时间:', item['jobDate'])
    #     print('----------------------------')
    #     return item
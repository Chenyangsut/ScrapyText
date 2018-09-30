# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

class RenrenPipeline(object):
    def process_item(self, item, spider):
        # curPath = 'f:/text/111'
        # file_name = str(item['title']) + '.txt'
        # file_path = curPath + '/' + file_name.decode('utf-8')
        # fp = open(file_path, 'w')
        # fp.write(item['title'] + '\n')
        # fp.close()
        pass

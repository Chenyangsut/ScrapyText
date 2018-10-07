# -*- coding: utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class ZhengdaoPipeline(object):
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

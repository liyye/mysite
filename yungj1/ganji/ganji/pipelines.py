# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb,time

class GanjiPipeline(object):
    def process_item(self, item, spider):
        # try:
            # time.sleep(0.2)
            # print(item['name'], item['sex'], item['profession'], item['worktime'], item['job'], item['salary'],item['workexp'], item['eduexp'], item['selfeva'], item['skill'])
        if item != None:
            self.cursor.execute('insert into t_gj values("%s","%s","%s","%s","%s","%s","%s")', (item['name'], item['sex'], item['age'], item['edu'], item['addr'], item['excjob'], item['excsalary']))
            self.conn.commit()
            print('gj')
        else:
            pass
        # except:
        #     print('重复')
        #     pass

    def open_spider(self, spider):
        self.conn = MySQLdb.connect(host='localhost', port=3306, user='root', password='123', db='yunyun',charset='utf8')
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class TutorialPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.Connect(host='localhost', port=3306,
                                    user='root', password='123',
                               db='papa', charset='utf8')
        self.cursor = self.conn.cursor()
        self.sql = 'insert into job1 values(%s,%s,%s,%s,%s,%s,%s)'
    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (item['job1'], item['job11'], item['job2'], item['job3'], item['job4'], item['job5'], item['job6']))
        self.conn.commit()
        # self.cursor.close()
        # self.conn.close()

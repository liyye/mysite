# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

# conn = MySQLdb.Connect(host='localhost', port=3306,
#                                     user='root', password='123',
#                                db='papa', charset='utf8')
# cursor = conn.cursor()
# sql = 'insert into job1 values(%s,%s,%s,%s,%s,%s,%s)'

class TutorialPipeline(object):  # 千万要注意  记得在settings.py文件中进行设置
    def __init__(self,host,port,user,password,db,charset): # 2
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.db=db
        self.charset=charset

    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (item['job1'], item['job11'], item['job2'], item['job3'], item['job4'], item['job5']))
        self.conn.commit()

    # 当爬虫开启的时候自动调用该方法
    def open_spider(self, spider):  # 3
        # 数据库初始化
        self.conn = MySQLdb.Connect(host=self.host, port=self.port,
                                    user=self.user, password=self.password,
                                    db=self.db, charset=self.charset)
        self.cursor = self.conn.cursor()
        self.sql = 'insert into job58 values(%s,%s,%s,%s,%s,%s)'

    # 当spider关闭时自动调用
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

    # 该方法用于创建pipeline对象  1
    @classmethod
    def from_crawler(cls, crawler):  # 是一个类方法
        host = crawler.settings.get('HOST', 'localhost')
        port = crawler.settings.get('PORT', 3306)
        user = crawler.settings.get('USER', 'root')
        password = crawler.settings.get('PASSWORD', '123')
        db = crawler.settings.get('DB', 'papa')
        charset = crawler.settings.get('CHARSET', 'utf8')
        try:
            MySQLdb.Connect(host=host, port=port, user=user, password=password, db=db, charset=charset)
            return cls(host=host, port=port, user=user, password=password, db=db, charset=charset)
        except:
            return None


# 去重
from scrapy.exceptions import DropItem
class DropPipeline:
    def __init__(self):
        self.temp = set()  # 设置空集合
    def process_item(self,item,spider):
        # 去重？   集合
        # item: 字典 通过数据的内容判别是否重复
        data=item['job1']+item['job4']
        if data in self.temp:
            # 重了 扔掉
            return DropItem('该item已经存在')
        else:
            self.temp.add(data)
            return item

import jieba
import jieba.analyse as ja
# 清洗
class CleanPipeline:
    def process_item(self,item,spider):
        # 去除不要的字符串
        # item['jobMessage']=''.join(r.findall(item['jobMessage']))

        # 2提取关键字
        item['job1']='/'.join(ja.extract_tags(item['job1'],topK=2))
        item['job11']='/'.join(ja.extract_tags(item['job11'],topK=10))
        item['job2']='/'.join(ja.extract_tags(item['job2'],topK=10))
        item['job3']='/'.join(ja.extract_tags(item['job3'],topK=30))
        item['job4']='/'.join(ja.extract_tags(item['job4'],topK=30))
        # item['job5']='/'.join(ja.extract_tags(item['jobMessage'],topK=30))
        return item
        # 3 添加数据
        # if item['jobMessage']=='':
        #     item['jobMessage']='无'

import time
import datetime
class DatePipeline:

    def process_item(self,item,spider):
        # 2019-7-10
        # item['date']
        # data1 = item['job5']
        # date1 = '今天'
        if item['job5'] == '今天':
            item['job5']=time.strftime('%Y-%m-%d')
            # date1=datetime.datetime.today()
        elif item['job5']==' 天前':
            item['job5']=time.strftime('%Y-%m-%d',time.localtime(time.time()-60*60*24))
            # date1=str(datetime.datetime.today()-datetime.timedelta(days=1))
        elif item['job5']==' 小时前':
            item['job5'] = time.strftime('%Y-%m-%d')
            # date1 = datetime.datetime.today()
        elif item['job5']==' 分钟前':
            item['job5'] = time.strftime('%Y-%m-%d')
        else:
            pass
        return item

















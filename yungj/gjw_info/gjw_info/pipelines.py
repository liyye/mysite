# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class GjwInfoPipeline(object):
    # def process_item(self, item, spider):
    #     return item
    def __init__(self, host, port, user, password, db, charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.conn = None
        self.cursor = None
        self.sql = None

    def process_item(self, item, spider):
        if item != None:
            self.cursor.execute(self.sql, (item['name'], item['sex'], item['age'], item['addr'],item['job'], item['salary'],item['edu']))
            self.conn.commit()
        else:
            pass


    def open_spider(self, spider):  # 3
        # 数据库初始化
        self.conn = MySQLdb.Connect(host=self.host, port=self.port,
                                    user=self.user, password=self.password,
                                    db=self.db, charset=self.charset)
        self.cursor = self.conn.cursor()
        self.sql = 'insert into t_gj values(%s,%s,%s,%s,%s,%s,%s)'

    # 当spider关闭时自动调用
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

    @classmethod
    def from_crawler(cls, crawler):  # 是一个类方法
        host = 'localhost'
        port = 3306
        user = 'root'
        password = '123'
        db = 'yunyun'
        charset = 'utf8'
        # print(host,port,user,password,db,charset)
        try:
            MySQLdb.Connect(host=host, port=port, user=user, password=password, db=db, charset=charset)
            # print('a'*80)
            return cls(host=host, port=port, user=user, password=password, db=db, charset=charset)
        except:
            return None


from scrapy.exceptions import DropItem
class DropPipeline:
    def __init__(self):
        self.temp = set()  # 设置空集合

    def process_item(self, item, spider):
        _ = spider
        # print('+'*100)
        # 去重？   集合
        # item: 字典 通过数据的内容判别是否重复
        if not item['name']:
            item['name'] = ''
        if not item['job']:
            item['job'] = ''
        # print(type(item['name']), type(item['job_intention']))
        data = item['name'] + item['job']
        if data in self.temp:
            # 重了 扔掉
            return DropItem('该item已经存在')
        else:
            # print('='*100)
            self.temp.add(data)
            # print(item)
            return item

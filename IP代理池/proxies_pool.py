
# ***思路***

# IP代理池：
# 数据库： 存ip 端口号 类型  proxy_pool
# 架构：类   提供IP：工具
# 编码：

# 功能： 1. 给用户提供代理   2. 检测IP是否可用  3. 爬取IP  4. 保存到数据库  5.检测代理池有多少可用的IP
# 6. 检测是否需要补充IP
import MySQLdb
import requests
from lxml import etree

class PorxyPool(object):
    # 属性
    # 测试网站URL
    TEST_URL = 'http://www.httpbin.org/ip'
    # 方法  普通方法  初始化方法
    def __init__(self,limit=3,volume=10,tartgetURL='https://www.xicidaili.com/nn/'):
        # 目标网站URL（提供IP）
        self.targetURL=tartgetURL
        # 数据库
        self.dbInit()
        # 阈值
        self.limit=limit
        # 设置初始页码
        self.pageNum=1
        # 设置容量
        self.volume=volume
        #发送本机IP，获得结果
        self.response=requests.get(url=self.TEST_URL).text  # self.*  调用属性

    # 数据库初始化
    def dbInit(self):
        # 创建链接
        self.conn=MySQLdb.connect(host='localhost',port=3306,
                                  user='root',password='123',
                                  db='papa',charset='utf8')
        # 创建游标
        self.cursor=self.conn.cursor()

    # 爬取IP
    def getOneIP(self):  # getter
        while 1:
            res=requests.get(self.targetURL+str(self.pageNum)) # url拼接页码
            self.pageNum+=1
            if 2500<self.pageNum:
                self.pageNum=1
            e=etree.HTML(res.text)
            # 获取tr标签
            trs=e.xpath('//tr[@class="odd"]') # trs 是个列表
            for tr in trs:
                ip,port,types=tr.xpath('//td[2]/text() | //td[3]/text() | //td[6]/text()')
                # 测试
                if self.checkIP(ip,port,types):
                    # 可用：入库
                    # 入库
                    self.cursor.execute('insert into xici values(%s,%s,%s,1)',(ip,port,types))
                else:
                    pass

            if self.getAllProxyAvailable()==self.volume:
                break


    # 检查是否可用
    def checkIP(self,ip,port,types):
        try:
            response=requests.get(url=self.TEST_URL,proxies={types:ip+':'+port}).text
            if self.response==response:
                # 不可用
                return False
            else:
                return True
        except:
            return False

    #获得所有可用ip数量
    def getAllProxyAvailable(self):
        # 查看所有状态为1的数据
        self.cursor.execute('select count(*) from xici where status=1')
        # resultNumber = self.cursor.fetchone()[0]
        resultNumber = self.cursor.fetchall()[0]
        return resultNumber
    # 给用户提供IP
    def api(self):
        # 从数据库取出一个可用IP并返回
        self.cursor.execute('select ip,port,types from xici where status=1 limit 1')
        #
        # result=self.cursor.fetchone() # (ip,port,types)
        result=self.cursor.fetchall() # (ip,port,types)
        # 将本数据修改状态
        self.cursor.execute("update xici set status=0 where ip=('%s')" %result[0])
        self.conn.commit()
        # 判断是否达到阈值，并进行补充
        self.appendProxy()
        return result

    #判断阈值，补充数据
    def appendProxy(self):
        if self.getAllProxyAvailable()<self.limit:
            # 进行补充，爬去数据
            self.getOneIP()

    def checkRegular(self):  # 一定要使用多线程
        from apscheduler.schedulers.blocking import BlockingScheduler
        sch=BlockingScheduler()
        def fun():
            self.cursor.execute('select ip,port,types from xici')
            for i in self.cursor.fetchall():  # i:每条数据
                # 检查是否可用
                if self.checkIP(i):
                    self.cursor.execute("update xici set status=1 where ip=('%s')" %i[0])

                else:
                    self.cursor.execute("update xici set status=0 where ip=('%s')" %i[0])

                self.conn.commit()
            self.appendProxy()
        sch.add_job(fun,'cron',second='*/600')
        sch.start()



if __name__ == '__main__':
    import  threading
    pp=PorxyPool()
    # threading.Thread(target=pp.checkRegular,daemon=True).start()
    pp.checkRegular()












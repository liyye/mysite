import requests
from lxml import etree
from multiprocessing import Pool,Manager,Queue,Process
import time
import MySQLdb

# conn = MySQLdb.Connect(host='localhost',port=3306,user='root',password='123456',db='crawler',charset='utf8')
# cursor = conn.cursor()

url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

def get_list(q_url):
    #获取详情页的url
    res = requests.get(url=url)
    ele = etree.HTML(res.text)
    detail_urls = ele.xpath('//p[@class="t1 "]/span[1]/a/@href')
    for i in detail_urls:
        q_url.put(i)


def get_detail(q_url,q_data):

    while 1:
        url = q_url.get()
        res = requests.get(url=url)
        ele = etree.HTML(res.text)
        title = ele.xpath('//div[@class="cn"]/h1/@title')
        q_data.put(title[0])

def in_db(q_data):

    #入库
    while 1:
        print(q_data.get())
    #     sql = 'insert into job51 values (%s,1)'
    #     cursor.execute(sql,(q_data.get(),))
    #     conn.commit()


if __name__ == '__main__':
    pool = Pool(processes=3)
    q = Queue(maxsize=1)
    q_url = Manager().Queue()
    q_data = Manager().Queue()
    pool.apply_async(func=get_list,args=(q_url,))
    pool.apply_async(func=get_detail,args=(q_url,q_data))
    pool.apply_async(func=in_db,args=(q_data,))
    pool.close()
    pool.join()
    # cursor.close()
    # conn.close()

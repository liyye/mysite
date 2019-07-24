import requests
import re
import time

import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='papa', charset='utf8')
cursor = conn.cursor()

conn1 = MySQLdb.connect(host='172.16.11.21', port=3306, user='root', passwd='123', db='hero', charset='utf8')
cursor1 = conn1.cursor()

cursor.execute("select wanzhan from tianmao ")
a1 = cursor.fetchall()
# for i in a1:
#     t=(i[0])
#     # url='https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15436921628.149.3eea658bzBf2kN&id=590521148160&rn=3cc2c9c58e867db7b8591f8a98938a72&abbucket=10'
#     url=t
#     a=requests.get(url)
#     pr=a.text
#     pattern = re.compile('"reservePrice":"(.*?)"')
#     rev1 = pattern.findall(pr)
#     print(rev1[0]) #价格
#     cursor.execute("select shumin,dianpu from tianmao where wanzhan='%s'"%t)
#     a11 = cursor.fetchall()
#     # print(a11)
#     print(a11[0][0]) #书名
#     print(a11[0][1]) #店铺
#     print(t) #地址
#     q1=a11[0][0]
#     q2=rev1[0]
#     q4=a11[0][1]
#     sql1 = "insert into checkbook_book1(bookname,bookprice,shopurl,shopname) VALUES (%s,%s,%s,%s)"
#     row_count = cursor1.execute(sql1, (q1,q2,t,q4))
#     conn1.commit()

# url='https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-17458772281.140.720d71ef3Dfgoj&id=571685187028&rn=2f394a53618f96af5d402b6f8d281f94&abbucket=10'
# # url=t
# a=requests.get(url)
# pr=a.text
# print(pr)

with 1:
    time.sleep(60*30)
    for i in a1:
        t=(i[0])
        # url='https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15436921628.149.3eea658bzBf2kN&id=590521148160&rn=3cc2c9c58e867db7b8591f8a98938a72&abbucket=10'
        url=t
        a=requests.get(url)
        pr=a.text
        pattern = re.compile('"reservePrice":"(.*?)"')
        rev1 = pattern.findall(pr)
        print(rev1[0]) #价格
        cursor.execute("select shumin,dianpu from tianmao where wanzhan='%s'"%t)
        a11 = cursor.fetchall()
        # print(a11)
        print(a11[0][0]) #书名
        print(a11[0][1]) #店铺
        print(t) #地址
        q1=a11[0][0]
        q2=rev1[0]
        q4=a11[0][1]
        sql1 = "update checkbook_book1 set bookprice='%s' where shopurl=('%s')"%(q2,t)
        row_count = cursor1.execute(sql1)
        conn1.commit()










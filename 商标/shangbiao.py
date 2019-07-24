import requests as req
import json

import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='papa', charset='utf8')
cursor = conn.cursor()

url="http://sbgg.saic.gov.cn:9080/tmann/annInfoView/annSearchDG.html"

headers={
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Content-Length': '277',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': '__jsluid_h=04d4d687a18cb9408a4462479821ab38; Hm_lvt_d7682ab43891c68a00de46e9ce5b76aa=1563284298,1563284341; Hm_lpvt_d7682ab43891c68a00de46e9ce5b76aa=1563284341; tmas_cookie=51947.7703.15402.0000; JSESSIONID=000080ZK2DfJ3-ibqDmo5s62Of3:1bm104t91',
'Host': 'sbgg.saic.gov.cn:9080',
'Origin': 'http://sbgg.saic.gov.cn:9080',
'Referer': 'http://sbgg.saic.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum=1647',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest',

}

for j in range(1,23):
    data={
        'page': j,
        'rows': 10000,
        'annNum': 1647,
        'annType': '',
        'tmType': '',
        'coowner': '',
        'recUserName': '',
        'allowUserName': '',
        'byAllowUserName': '',
        'appId': '',
        'appIdZhiquan': '',
        'bfchangedAgengedName': '',
        'changeLastName': '',
        'transferUserName': '',
        'acceptUserName': '',
        'regName': '',
        'tmName': '',
        'intCls': '',
        'fileType':'' ,
        'totalYOrN': 'true',
        'appDateBegin': '',
        'appDateEnd': '',
        'agentName': ''
    }

    re=req.post(url=url,data=data,headers=headers).text
    # print(re)
    a=json.loads(re)
    a1=a['rows']
    # print(a1)
    for i in a1:
        # print(i)
        a2=i['reg_name']
        a3=i['reg_num']
        print(a2,a3)
        sql = "insert into zgsb1 values(%s,%s)"
        row_count = cursor.execute(sql, (a2,a3))
    conn.commit()











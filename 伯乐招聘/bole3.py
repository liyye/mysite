import re
import requests
from lxml import etree
from my_fake_useragent import UserAgent
import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='yunyun', charset='utf8')
cursor = conn.cursor()


a=UserAgent()
p=a.random()
headers = {
            'User-Agent': p,
            # 'cookie': '__cfduid=dce1ed34975ff71acb9b22d4959d0263b1563521810; ASP.NET_SessionId=1oj0zvk0wttwcudymxjeftpt; UM_distinctid=16c0928d2b2448-03463007e150d9-e343166-144000-16c0928d2b32f6; CNZZDATA1255263807=653621382-1563520703-%7C1563520703; ViewHistory_4=1oj0zvk0wttwcudymxjeftpt; .ynzpauth=869D169A9273686FE3F281194E66EAF796DA177B8799BC0686C9AFD983575676620178F545B8CC60F7FEAA6886B258DF06E4D0E13BBE33ABBA3DCF46FB3A659EE847BBE2696F2256B15111D8D1BDD642178E9567CF7161BDEA9BC44159707D7DF2F8D7D349B8397F87AA820265CC36F284BFECA0EF6E38D76411703DA70E1B5EB03806C9211CD2EC6C800D8E4E9CC840A8734ACC7E31910E493DCF0B2D859E27; viewedResume=2088560%2C1515707%2C727002%2C1218946%2C1623681%2C2131167%2C2121066'
}

for i in range(30052,38001):
    url='http://www.bole.com.cn/resume/resume-show.php?id='+str(i)+''
    # print
    try:
        with requests.session() as s:
            a=s.get(url,headers=headers)
            pr=a.text
            # print(pr)
            pattern = re.compile('<div class="personal_info_item">(.*?)</div>')
            rev1 = pattern.findall(pr)
            # print(rev1)
            t=rev1[0]
            t1=rev1[1]
            t2=rev1[2]
            t3=rev1[6]
            t4=rev1[7]
            t5=rev1[9]
            t6=rev1[10]
            t7=rev1[11]
            t8=rev1[12]
            t9=rev1[13]
            print(t)
            print(t1)
            print(t2)
            print(t3)
            print(t4)
            print(t5)
            print(t6)
            print(t7)
            print(t8)
            print(t9)
            h=etree.HTML(a.text)
            # q1=h.xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/div[2]/div[2]/comment()[1]//text()')
            q1=h.xpath('/html/body/div[4]/div/div[1]/div[2]/div[2]/div[2]/p[1]/text()')
            print(q1[0])
            q2 = h.xpath('/html/body/div[4]/div/div[1]/div[2]/div[2]/div[2]/p[2]/text()')
            print(q2[0])
            q3 = h.xpath('/html/body/div[4]/div/div[1]/div[2]/div[2]/div[2]/p[3]/text()')
            print(q3[0])
            q4 = h.xpath('/html/body/div[4]/div/div[1]/div[2]/div[2]/div[2]/p[4]/text()')
            print(q4[0])
            q5 = h.xpath('/html/body/div[4]/div/div[1]/div[2]/div[2]/div[2]/p[5]/text()')
            q5 = ''.join(q5)
            print(q5)
            q6 = h.xpath('/html/body/div[4]/div/div[1]/div[2]/div[3]//text()')
            q6 = [''.join([i.strip() for i in price.strip().split('\t')]) for price in q6]
            q6 = ''.join(q6)
            print(q6)
            q7 = h.xpath('/html/body/div[4]/div/div[1]/div[2]/div[4]//text()')
            q7 = [''.join([i.strip() for i in price.strip().split('\t')]) for price in q7]
            q7 = ''.join(q7)
            print(q7)
            q8 = h.xpath('/html/body/div[4]/div/div[1]/div[2]/div[5]//text()')
            q8 = [''.join([i.strip() for i in price.strip().split('\t')]) for price in q8]
            q8 = ''.join(q8)
            print(q8)
            sql1 = "insert into bole VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            row_count = cursor.execute(sql1, (t,t1,t2,t3,t4,t5,t6,t7,t8,t9,q1,q2,q3,q4,q5,q6,q7,q8))
            conn.commit()
            print(i)

    except:
        print('########################')
import requests
from lxml import etree
# from .chaojiying import getcode
from renren.人人.chaojiying import getcode

import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='papa', charset='utf8')
cursor = conn.cursor()

url='http://www.renren.com/880151247/profile'

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'cookie': 'anonymid=jy3rzgk0cxg1vf; depovince=BJ; _r01_=1; jebe_key=7cd70cf6-ae4d-479e-892e-45ed31eb8e0b%7C8c211f2781aa4194b4b15ed74948caa0%7C1563158247255%7C1%7C1563158204445; jebe_key=7cd70cf6-ae4d-479e-892e-45ed31eb8e0b%7C8c211f2781aa4194b4b15ed74948caa0%7C1563158247255%7C1%7C1563158204448; wp=1; l4pager=0; JSESSIONID=abcxll3qfKoYQfFphp4Vw; ick_login=93800d9f-5da3-41c9-a1b3-7caf5b642239; t=4bd613114b014b10df73a9d6a1c1ded33; societyguester=4bd613114b014b10df73a9d6a1c1ded33; id=971493113; xnsid=7c24814; jebecookies=36209791-eea6-40db-9cc7-48f97e5015e3|||||; ver=7.0; loginfrom=null; wp_fold=0'
}

def qr():
    with requests.session() as s:
        cursor.execute("select url from t_url where zt='1'")
        a1 = cursor.fetchall()
        # print(len(a1))
        # print(a1[0][0],'5757')
        for i in range(len(a1)):
            w='http://www.renren.com/' + a1[i][0] + '/profile'
            # print(w)
            a = s.get(w, headers=headers)
            # print(a.text)
            h = etree.HTML(a.text)

            try:
                code = h.xpath('//label[@for="personalInfo5qValidateCode"]/text()')[0]
            except:
                code = ''
            print(code)
            if '验证码:' == code:
                # print(h.text)
                img_src = h.xpath('//img/@src')[1]
                # img_src = 'http://icode.renren.com/getcode.do?t=ninki&rnd=1563186658140'
                print(img_src)
                with open('t.jpg','wb') as w:
                    w.write(s.get(url=img_src).content)
                with open('t.jpg','rb') as r:
                    im = r.read()
                c = getcode(im)['pic_str']
                print(c)
                data = {
                    # 'id':880792860,
                    'icode' : c,
                    'submit': '继续浏览',
                    'requestToken': '1877362478',
                    '_rtk': '3ba74588'
                }
                print(data)
                res = s.post(url='http://www.renren.com/validateuser.do',data=data,headers=headers)
                res_people = s.get(url='http://www.renren.com/254502398/profile',headers=headers)
                print(res_people.text)

            f1 = h.xpath('//div[@class="cover-bg"]/h1/text()')
            try:
                f1 = [''.join([i.strip() for i in price.strip().split('\t')]) for price in f1][0]

                # job6 = ''.join(job6)
                f2 = h.xpath('//div[@class="tl-information"]//text()')
                f2 = [''.join([i.strip() for i in price.strip().split('\t')]) for price in f2]
                b = []
                for i in f2:
                    if i != '':
                        b.append(i)
                        # print(b)
                b = ' '.join(b)
                if b=='':
                    b='无'
                print(f1)
                print(b)
                # cc=a1[i][0]
                sql = "insert into t_people VALUES (%s,%s)"
                row_count = cursor.execute(sql, (f1, b))
                # sql2="update t_url set zt='0' where url='{url1}'".format(url1=cc)
                # cursor.execute(sql2)
                conn.commit()

            except:
                pass

qr()

def qq(ur):
    with requests.session() as s:
        a = s.get(ur, headers=headers)
        # print(a.text)
        h = etree.HTML(a.text)
        w1 = []
        try:
            q1 = h.xpath('//div[@class="clearfix"]/ul//li/a/@namecard')
            for i in q1:
                try:
                    sql = "insert into t_url VALUES (%s,%s)"
                    row_count = cursor.execute(sql, (i,1))
                    conn.commit()
                    # qr()
                    w1.append('http://www.renren.com/' + i + '/profile')
                except:
                    pass
        except:
            pass
        try:
            q2 = h.xpath('//div[@class="clearfix"]/ul//li/a/@namecard')
            for j in q2:
                try:
                    sql = "insert into t_url VALUES (%s,%s)"
                    row_count = cursor.execute(sql, (j, 1))
                    conn.commit()
                    # qr()
                    w1.append('http://www.renren.com/' + j + '/profile')
                except:
                    pass
        except:
            pass
        try:
            q3 = h.xpath('//div[@class="has-friend"]/ul//li/a/@namecard')
            for q in q3:
                try:
                    sql = "insert into t_url VALUES (%s,%s)"
                    row_count = cursor.execute(sql, (q, 1))
                    conn.commit()
                    # qr()
                    w1.append('http://www.renren.com/' + q + '/profile')
                except:
                    pass
        except:
            pass

        for p in w1:
            print(p)
            # qr(p)
            qq(p)

# qq(url)


# if __name__ == '__main__':
#     qq(url)




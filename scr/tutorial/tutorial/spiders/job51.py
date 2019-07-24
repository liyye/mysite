# -*- coding: utf-8 -*-
import scrapy
import scr.tutorial.tutorial.items as items
import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='papa', charset='utf8')
cursor = conn.cursor()
cursor.execute("select index1 from jobindex")
a = cursor.fetchone()
kwIndex1 = a[0]
class Job51Spider(scrapy.Spider):
    name = 'job51'
    allowed_domains = ['http://www.51job.com']
    start_urls = ['https://www.51job.com/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Cookie': 'guid=5909bf59bc613437bc6aa94adbb355a2; adv=adsnew%3D1%26%7C%26adsresume%3D1%26%7C%26adsfrom%3Dhttp%253A%252F%252Fwww.baidu.com%252Fbaidu.php%253Furl%253Daf0000aF4eAvq9HI8kuJpM82EhKZ4UPOpFkPCpAg2DMiDyL9x4g16lxy4uIJouqDQgCN2dMFHa5G9gZpyyNOUjYAE6NEZS3lJcPsWxjIpNP04XEOTYh6w4yFDklWGOF0HgkZeG4L6k8jpuvKiixT4WFrR38LL0UD-HfdyC9eG_NSu0lR9FaVUAYs2KReLVlkpH4uZf-j-cFH17VtU0.Db_NR2Ar5Od66CHnsGtVdXNdlc2D1n2xx81IZ76Y_u2SMu3e8MJ1-k_nOEOlecxLO3MHSEwECntx135zOCxgvg45E6OeAHxfOgkOdkxo3O-CLOWEWEzgxwOsr5Oml5dlpoQOvSajSw7OVxwxS9yOO_xVYXveqElqEgVmvfdG_H3en-dvHFIjxvuQVOB-MFb8lRq5uEtNBmzUo2OA1Fk4xZ-8dQjPakbLtU57f0.U1Yz0ZDqPH7JUvc0TA-W5H00IjdJUvcdnfKGUHYznjf0u1dEugK1nfKdpHdBmy-bIykV0ZKGujYk0APGujY1rHD0UgfqnH0kPdtknjD4g1csPWFxnHDsPj7xn10sP-t1PW0k0AVG5H00TMfqPH6v0ANGujYkPjmzg1cknj6vg1c4nWnLg1c3PHD3g1c4njb4g1c3rjndg1c4nWcs0AFG5HDdr7tznjf0UynqrjcYnH0YPjczg1Dsnj7xPWn1rjRznjbYg1fsg1Dsn-ts0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5Hc0TZ0qn0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5H00ThCqn0KbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqnH00UMfqn0K1XWY0mgPxpywW5gK1QyPV0A-bm1dcfbD0IZN15HD1n16YP1mkP1fznHDvnH0vn1nk0ZF-TgfqnHRvnWmvPW0Yn1R3PfK1pyfqmWTLn1bYPHfsnjK-uAwWP6KWTvYqn1bsnRmLPj-aPH04n1nsfsK9m1Yk0ZK85H00TydY5H00Tyd15H00XMfqn0KVmdqhThqV5HKxn7tsg1Kxn10knNts0Aw9UMNBuNqsUA78pyw15HKxn7tsg1csPHckn7t1n16YnWbLg100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYs0AuWIgfqn0KhXh6qn0Khmgfqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0AqY5H00ULFsIjYsc10Wc10Wnansc108nj0snj0sc10W0APzm1YdnHnsP6%2526word%253D51job%2526ck%253D1935.7.109.394.322.342.236.259%2526shh%253Dwww.baidu.com%2526sht%253D25017023_7_dg%2526us%253D2.4480.3.0.3.1497.0%2526bc%253D110101%26%7C%26adsnum%3D2168756; partner=www_baidu_com; 51job=cenglish%3D0%26%7C%26; search=jobarea%7E%60010000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%601%A1%FB%A1%FA010000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1562666130%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D',
        'Referer': 'https://www.51job.com/'
    }

    def parse(self, response):
        for kwIndex11 in range(301,310):


            url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,' + str(kwIndex11) + '.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=4&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

        # 'https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=' \
            # 'https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
            # 'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=4&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

            yield scrapy.Request(url=url,callback=self.parListPage,headers=self.headers,dont_filter=True)

    def parListPage(self,response):
        # print('********')
        res=response.xpath('//p[@class="t1 "]/span/a/@href').extract()
        for i in res:
            yield scrapy.Request(url=i,dont_filter=True,callback=self.dataParse,headers=self.headers)
        # cursor.execute("select index1 from jobindex")
        # a = cursor.fetchone()
        # kwIndex1 = a[0]
        # kwIndex1 += 1
        # cursor.execute("update t_index set start=('%s')" % kwIndex1)
        # conn.commit()
    def dataParse(self,response):
        # print('进入详情页！！！')
        job1=response.xpath('//h1/@title').extract()[0]
        job11=response.xpath('//p[@class="cname"]/a/@title').extract()[0]
        job2=response.xpath('//div[@class="cn"]/strong/text()').extract()[0]
        job3 = response.xpath('string(//p[@class="msg ltype"])').extract()[0]
        job3 = "".join(job3.split())
        job4=response.xpath('string(//div[@class="bmsg job_msg inbox"])').extract()
        job4 = [''.join([i.strip() for i in price.strip().split('\t')]) for price in job4][0]
        job5 = response.xpath('string(//div[@class="tBorderTop_box"][2])').extract()
        job5 = [''.join([i.strip() for i in price.strip().split('\t')]) for price in job5][0]
        job6 = response.xpath('string(//div[@class="tBorderTop_box"][3])').extract()
        job6 = [''.join([i.strip() for i in price.strip().split('\t')]) for price in job6][0]

        print(job1)
        print(job11)
        print(job2)
        print(job3)
        print(job4)
        print(job5)
        print(job6)

        i = items.TutorialItem()
        i['job1'] = job1
        i['job11'] = job11
        i['job2'] = job2
        i['job3'] = job3
        i['job4'] = job4
        i['job5'] = job5
        i['job6'] = job6
        return i  # 返回了一个Item对象











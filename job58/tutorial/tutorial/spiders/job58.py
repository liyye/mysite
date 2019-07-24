# -*- coding: utf-8 -*-
import scrapy
import job58.tutorial.tutorial.items as items
import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='papa', charset='utf8')
cursor = conn.cursor()
cursor.execute("select index1 from jobindex")
a = cursor.fetchone()
kwIndex1 = a[0]
class Job51Spider(scrapy.Spider):
    name = 'job58'
    allowed_domains = ['https://bj.58.com/']
    start_urls = ['https://bj.58.com/']
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    #     'Cookie': 'guid=5909bf59bc613437bc6aa94adbb355a2; adv=adsnew%3D1%26%7C%26adsresume%3D1%26%7C%26adsfrom%3Dhttp%253A%252F%252Fwww.baidu.com%252Fbaidu.php%253Furl%253Daf0000aF4eAvq9HI8kuJpM82EhKZ4UPOpFkPCpAg2DMiDyL9x4g16lxy4uIJouqDQgCN2dMFHa5G9gZpyyNOUjYAE6NEZS3lJcPsWxjIpNP04XEOTYh6w4yFDklWGOF0HgkZeG4L6k8jpuvKiixT4WFrR38LL0UD-HfdyC9eG_NSu0lR9FaVUAYs2KReLVlkpH4uZf-j-cFH17VtU0.Db_NR2Ar5Od66CHnsGtVdXNdlc2D1n2xx81IZ76Y_u2SMu3e8MJ1-k_nOEOlecxLO3MHSEwECntx135zOCxgvg45E6OeAHxfOgkOdkxo3O-CLOWEWEzgxwOsr5Oml5dlpoQOvSajSw7OVxwxS9yOO_xVYXveqElqEgVmvfdG_H3en-dvHFIjxvuQVOB-MFb8lRq5uEtNBmzUo2OA1Fk4xZ-8dQjPakbLtU57f0.U1Yz0ZDqPH7JUvc0TA-W5H00IjdJUvcdnfKGUHYznjf0u1dEugK1nfKdpHdBmy-bIykV0ZKGujYk0APGujY1rHD0UgfqnH0kPdtknjD4g1csPWFxnHDsPj7xn10sP-t1PW0k0AVG5H00TMfqPH6v0ANGujYkPjmzg1cknj6vg1c4nWnLg1c3PHD3g1c4njb4g1c3rjndg1c4nWcs0AFG5HDdr7tznjf0UynqrjcYnH0YPjczg1Dsnj7xPWn1rjRznjbYg1fsg1Dsn-ts0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5Hc0TZ0qn0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5H00ThCqn0KbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqnH00UMfqn0K1XWY0mgPxpywW5gK1QyPV0A-bm1dcfbD0IZN15HD1n16YP1mkP1fznHDvnH0vn1nk0ZF-TgfqnHRvnWmvPW0Yn1R3PfK1pyfqmWTLn1bYPHfsnjK-uAwWP6KWTvYqn1bsnRmLPj-aPH04n1nsfsK9m1Yk0ZK85H00TydY5H00Tyd15H00XMfqn0KVmdqhThqV5HKxn7tsg1Kxn10knNts0Aw9UMNBuNqsUA78pyw15HKxn7tsg1csPHckn7t1n16YnWbLg100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYs0AuWIgfqn0KhXh6qn0Khmgfqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0AqY5H00ULFsIjYsc10Wc10Wnansc108nj0snj0sc10W0APzm1YdnHnsP6%2526word%253D51job%2526ck%253D1935.7.109.394.322.342.236.259%2526shh%253Dwww.baidu.com%2526sht%253D25017023_7_dg%2526us%253D2.4480.3.0.3.1497.0%2526bc%253D110101%26%7C%26adsnum%3D2168756; partner=www_baidu_com; 51job=cenglish%3D0%26%7C%26; search=jobarea%7E%60010000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%601%A1%FB%A1%FA010000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1562666130%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D',
    #     'Referer': 'https://www.51job.com/'
    # }

    def parse(self, response):
        # url1 = 'https://bj.58.com/job/pn1/pve_5363_247_pve_5358_0/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&key=&PGTID=0d302408-0000-1175-b9a1-4f148d2f63ab&ClickID=2'
        # scrapy.Request(url=url1, callback=self.parListPage, dont_filter=True)
        # a=response.xpath('//span[@class="num_operate"]/i/text()').extract()[0]
        # a=int(a)
        a=['bj','sh','gz','sz','cd','hz','nj','tj','wh','cq']
        for i in a:
            for kwIndex11 in range(1,70):
                url = 'https://' + i + '.58.com/job/pn' + str(kwIndex11) + '/pve_5363_247_pve_5358_0/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&key=&PGTID=0d302408-0000-1175-b9a1-4f148d2f63ab&ClickID=2'

                yield scrapy.Request(url=url,callback=self.parListPage,dont_filter=True)

    def parListPage(self,response):
        # print(response)
        a=response.xpath('//span[@class="num_operate"]/i/text()').extract()[0]
        # print(a)
        res=response.xpath('//div[@class="job_name clearfix"]/a/@href').extract()
        for i in res:
            # print(i)
            yield scrapy.Request(url=i,dont_filter=True,callback=self.dataParse)

    def dataParse(self,response):
        # print('进入详情页！！！')
        job1=response.xpath('//div[@class="pos_base_info"]/span/text()').extract()[0]
        job1 = job1.strip()
        job12 = response.xpath('//div[@class="pos_base_info"]/span[2]/text()').extract()[0]
        job12 = job12.strip()
        job11=response.xpath('string(//div[@class="pos_welfare"])').extract()[0]
        job11=job11.strip()
        job2=response.xpath('string(//div[@class="pos_base_condition"])').extract()[0]
        job2 = job2.strip()
        job3 = response.xpath('string(//div[@class="subitem_con pos_description"])').extract()
        job3 = [''.join([i.strip() for i in price.strip().split('\t')]) for price in job3][0]
        job4=response.xpath('string(//div[@class="subitem_con comp_intro"])').extract()
        job4 = [''.join([i.strip() for i in price.strip().split('\t')]) for price in job4][0]
        job5 = response.xpath('//span[@class="pos_base_num pos_base_update"]/span/text()').extract()[0]


        print(job1)
        print(job11)
        print(job2)
        print(job3)
        print(job4)
        print(job5)

        i = items.TutorialItem()
        i['job1'] = job1
        i['job11'] = job11
        i['job2'] = job2
        i['job3'] = job3
        i['job4'] = job4
        i['job5'] = job5

        return i  # 返回了一个Item对象











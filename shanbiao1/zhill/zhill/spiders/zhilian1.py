# -*- coding: utf-8 -*-
import scrapy
import json
import shanbiao1.zhill.zhill.items as items

'https://cx.ht.cn/home-index-comsearch-m-Home-skey-d2b58408c720b00b76da91b64c8af894-p-1.html'
'https://cx.ht.cn/home-index-comsearch-m-Home-skey-d2b58408c720b00b76da91b64c8af894-p-2.html'
url='https://cx.ht.cn/home-index-comsearch-m-Home-skey-d2b58408c720b00b76da91b64c8af894-p-1.html'
'searchKey=中'

class Zhilian1Spider(scrapy.Spider):
    name = 'zhilian1'
    allowed_domains = ['http://www.gbicom.cn']
    start_urls = ['http://www.gbicom.cn']

    def parse(self, response):
        for i in range(19522):
            print(i)
            'http://www.gbicom.cn/search/0/2/all/1/desc/3,,,,,1,0/1'
            url = 'http://www.gbicom.cn/search/0/2/all/1/desc/'+str(i)+',,,,,1,0/1'
            yield scrapy.Request(url=url, callback=self.parListPage, dont_filter=True)

    def parListPage(self,response):
        # print(response.text,'213123')
        pr=response.text
        # print(pr)
        job1 = response.xpath('//*[@id="select"]/div[2]/div[1]/dl[1]/dt/a/@href').extract()
        for i in job1:
            yield scrapy.Request(url='http://www.gbicom.cn'+i,dont_filter=True,callback=self.dataParse)


    def dataParse(self,response):
        # print('进入详情页！！！')
        try:
            job1 = response.xpath('//*[@id="content_header"]/div/div[1]/div[2]/div[1]/span/em/text()').get()
            print(job1)
            job11 = response.xpath('//*[@id="brandName"]/text()').get()
            print(job11)
            i = items.ZhillItem()
            i['job1'] = job1
            i['job11'] = job11
            return i  # 返回了一个Item对象

        except:
            print('********************')




















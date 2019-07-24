# -*- coding: utf-8 -*-
import scrapy
import json
import shanbiao.zhill.zhill.items as items

'https://cx.ht.cn/home-index-comsearch-m-Home-skey-d2b58408c720b00b76da91b64c8af894-p-1.html'
'https://cx.ht.cn/home-index-comsearch-m-Home-skey-d2b58408c720b00b76da91b64c8af894-p-2.html'
url='https://cx.ht.cn/home-index-comsearch-m-Home-skey-d2b58408c720b00b76da91b64c8af894-p-1.html'
'searchKey=中'

class Zhilian1Spider(scrapy.Spider):
    name = 'zhilian1'
    allowed_domains = ['https://cx.ht.cn']
    start_urls = ['https://cx.ht.cn']

    def parse(self, response):
        for i in range(11147):
            print(i)
            url = 'https://cx.ht.cn/home-index-comsearch-m-Home-skey-d2b58408c720b00b76da91b64c8af894-p-'+str(i)+'.html'
            yield scrapy.Request(url=url, callback=self.parListPage, dont_filter=True)

    def parListPage(self,response):
        # print(response.text,'213123')
        pr=response.text
        # print(pr)
        job1 = response.xpath('//ul[@class="box"]//li/a/@href').extract()
        for i in job1:
            yield scrapy.Request(url='https://cx.ht.cn'+i,dont_filter=True,callback=self.dataParse)


    def dataParse(self,response):
        # print('进入详情页！！！')
        try:
            job1 = response.xpath('/html/body/div[4]/div[1]/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/span/text()').get()
            print(job1)
            job11 = response.xpath('/html/body/div[4]/div[1]/table/tbody/tr[3]/td[2]/span/text()').get()
            print(job11)
            i = items.ZhillItem()
            i['job1'] = job1
            i['job11'] = job11
            return i  # 返回了一个Item对象

        except:
            print('********************')




















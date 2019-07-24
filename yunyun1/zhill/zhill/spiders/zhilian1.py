# -*- coding: utf-8 -*-
import scrapy
import json
import yunyun1.zhill.zhill.items as items

'http://www.gzrc.com.cn/myNew/resume/ResumePreview_yl1001.php?ResumeId=job10012071712108&r=b11bdbc97fe1d1f0350c9526455cf25bb1ba4&gjTag=3&SearchKey=it&readsourceflag=3&fromtype=gz&uid=cm1563627377977'
'http://www.gzrc.com.cn/myNew/resume/ResumePreview_yl1001.php?ResumeId=job10011785786808&gjTag=3&SearchKey=it&readsourceflag=3&fromtype=gz&uid=cm1563627377977'

class Zhilian1Spider(scrapy.Spider):
    name = 'zhilian1'
    allowed_domains = ['http://www.ynzp.com']
    start_urls = ['http://www.ynzp.com']

    def parse(self, response):
        for i in range(1400000,1500000):
            # print(i)
            url = 'http://www.ynzp.com/pr/'+str(i)+'.html'
            yield scrapy.Request(url=url, callback=self.parListPage, dont_filter=True)

    def parListPage(self,response):
        # print(response.text,'213123')
        # pr=response.text
        # print(pr)
        try:
            q1 = response.xpath('//*[@id="main"]/div[2]/ul/li[1]//text()')
            r = q1.extract()[0]
            r1 = q1.extract()[1]
            q1 = r + r1
            print(q1)
            q2 = response.xpath('//*[@id="main"]/div[2]/ul/li[3]/text()').get()
            print(q2)
            q3 = response.xpath('//*[@id="main"]/div[2]/ul/li[4]/text()[1]').get()
            print(q3)
            q4 = response.xpath('//*[@id="main"]/div[2]/ul/li[4]/text()[2]').get()
            print(q4)
            q5 = response.xpath('//*[@id="main"]/div[2]/ul/li[5]//text()')
            e = q5.extract()[0]
            e1 = q5.extract()[1]
            q5 = e + e1
            print(q5)
            q6 = response.xpath('//*[@id="main"]/div[2]/ul/li[6]/text()[1]').get()
            print(q6)
            q7 = response.xpath('//*[@id="main"]/div[2]/ul/li[6]/text()[2]').get()
            print(q7)
            q8 = response.xpath('//*[@id="main"]/div[2]/ul/li[8]/p/text()').get()
            print(q8)
            q9 = response.xpath('//*[@id="main"]/div[9]//text()').extract()
            q9 = [''.join([i.strip() for i in price.strip().split('\t')]) for price in q9]
            q9 = ''.join(q9)
            print(q9)
            i = items.ZhillItem()
            i['q1'] = q1
            i['q2'] = q2
            i['q3'] = q3
            i['q4'] = q4
            i['q5'] = q5
            i['q6'] = q6
            i['q7'] = q7
            i['q8'] = q8
            i['q9'] = q9
            return i  # 返回了一个Item对象
        except:
            print('#####################################')






















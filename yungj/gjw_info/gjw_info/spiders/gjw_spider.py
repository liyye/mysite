# -*- coding: utf-8 -*-
import scrapy
from ..url import url_list
import re
from ..items import GjwInfoItem
class GjwSpiderSpider(scrapy.Spider):
    name = 'gjw_spider'
    allowed_domains = ['http://bj.ganji.com/']
    start_urls = ['http://bj.ganji.com//']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Cookie': "statistics_clientid=me; ganji_uuid=3983696531279761349146; ganji_xuuid=95ecf234-7501-4684-82b9-863b4ce41102.1563693096421; cityDomain=bj; _wap__utmganji_wap_newCaInfo_V2=%7B%22ca_n%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_i%22%3A%22-%22%7D; simResStatus=%2C30%2C; lg=1; WantedListPageScreenType=1536; STA_DS=1; citydomain=bj; Hm_lvt_acb0293cec76b2e30e511701c9bf2390=1563694652; xxzl_deviceid=D6o0VTsWEVcj3%2BUo48CH4D1qABUOnMJzA3PX9FaL3qCLliEl8JZIk3QPqH0bfsv2; sscode=GM0MyAyOv5OeE75IGMbEjikh; GanjiUserName=%23qq_810111255; GanjiUserInfo=%7B%22user_id%22%3A810111255%2C%22email%22%3A%22%22%2C%22username%22%3A%22%23qq_810111255%22%2C%22user_name%22%3A%22%23qq_810111255%22%2C%22nickname%22%3A%22%5Cu5343%5Cu5c18%5Cu5239%22%7D; bizs=%5B%5D; GANJISESSID=hnp5af0s9a6nmui8otnkb9okbv; last_name=%23qq_810111255; Hm_lvt_655ab0c3b3fdcfa236c3971a300f3f29=1563764270; xxzl_smartid=2aaafbd1c5034c1048940dbb95c302f3; Hm_lvt_8da53a2eb543c124384f1841999dcbb8=1563764319; Hm_lvt_6f6548400acfbcc44a302e67525049f7=1563764843; Hm_lpvt_6f6548400acfbcc44a302e67525049f7=1563764843; Hm_lvt_655ab0c3b3fdcfa236c3971a300f3f29=1563765311; Hm_lvt_acb0293cec76b2e30e511701c9bf2390=1563765312; Hm_lpvt_655ab0c3b3fdcfa236c3971a300f3f29=1563765331; Hm_lpvt_acb0293cec76b2e30e511701c9bf2390=1563765378; __utma=32156897.1707766422.1563765392.1563765392.1563765392.1; __utmc=32156897; __utmz=32156897.1563765392.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); gj_footprint=%5B%5B%22%5Cu7535%5Cu8bdd%5Cu9500%5Cu552e%22%2C%22%5C%2Fzpdianhuaxiaoshou%5C%2F%22%5D%2C%5B%22%5Cu552e%5Cu524d%5Cu5de5%5Cu7a0b%5Cu5e08%22%2C%22%5C%2Fzpsqgongchengshi%5C%2F%22%5D%5D; zhaopin_lasthistory=zpshichangyingxiao%7Czpdianhuaxiaoshou; zhaopin_historyrecords=bj%7Czpdianhuaxiaoshou%7C-%2Cbj%7Czpsqgongchengshi%7C-; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A54696744669%2C%22kw%22%3A%22it%22%7D; SiftRecord['1563765544']=it%3C%E6%B1%82%E8%81%8C%E7%AE%80%E5%8E%86%3E%7C%7C%2Fqiuzhi%2Fs%2F_it%2F%3Ffrom%3Dzhaopin_indexpage; vip_version=new; Hm_lpvt_8da53a2eb543c124384f1841999dcbb8=1563765907; Hm_lpvt_655ab0c3b3fdcfa236c3971a300f3f29=1563767045; Hm_lpvt_acb0293cec76b2e30e511701c9bf2390=1563767045; ganji_login_act=1563767046174; __utmt=1; __utmb=32156897.7.10.1563765392"
    }
    def parse(self, response):
        for url in url_list:
            yield scrapy.Request(url=url,headers=self.headers,callback=self.get_detail_page_url,dont_filter=True)



            # break
    def get_detail_page_url(self,response):
        url = response.url.split('/')[2]
        details_url = response.xpath('//a[@class="fl"]/@href').getall()
        for i  in  details_url:
            yield scrapy.Request(url='http://'+url+i,headers=self.headers,callback=self.detail_page_info,dont_filter=True)
        try:
            next_url = response.xpath('//a[@class="next"]/@href').extract()[0]
            url = 'http://bj.ganji.com'+next_url
            yield scrapy.Request(url=url,callback=self.get_detail_page_url,dont_filter=True)
        except:
            pass
            # break
    def detail_page_info(self,response):
        try :
            name = response.xpath('//div[@class="name-line"]/strong/text()').get()
            sex = response.xpath('//div[@class="name-line"]/span[1]/text()').get()
            age = response.xpath('//div[@class="name-line"]/span[2]/text()').get()
            edu = response.xpath('//div[@class="college-line clearfix"]/div[@class="left-box"]/b/text()').get()
            salary = response.xpath('//div[@class="salary-line clearfix"]/div[@class="left-box"]/b/text()').get()
            job1 = response.xpath('string(//div[@class="tend-line clearfix"])').get()
            r = re.compile('\S*')
            job = ''.join(r.findall(job1))
            addr1 = response.xpath('string(//div[@class="salary-line clearfix"]/div[@class="right-box"]/b)').get()
            r = re.compile('\S*')
            addr = ''.join(r.findall(addr1))
            print(name,sex,age,addr,job,salary,edu)
            i = GjwInfoItem()
            i['name'] = name
            i['sex'] = sex
            i['age'] = age
            i['addr'] = addr
            i['job'] = job
            i['salary'] = salary
            i['edu'] = edu
            return i
        except Exception as e:

            _ = e
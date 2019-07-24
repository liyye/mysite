# -*- coding: utf-8 -*-
import scrapy, time
from yungj2.ganji.ganji import items as items


class GanjispiderSpider(scrapy.Spider):
    name = 'ganjispider'
    allowed_domains = ['cd.ganji.com/qiuzhi/']
    start_urls = ['http://cd.ganji.com/qiuzhi/']
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'statistics_clientid=me; ganji_uuid=3983696531279761349146; ganji_xuuid=95ecf234-7501-4684-82b9-863b4ce41102.1563693096421; cityDomain=bj; _wap__utmganji_wap_newCaInfo_V2=%7B%22ca_n%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_i%22%3A%22-%22%7D; lg=1; WantedListPageScreenType=1536; STA_DS=1; xxzl_deviceid=D6o0VTsWEVcj3%2BUo48CH4D1qABUOnMJzA3PX9FaL3qCLliEl8JZIk3QPqH0bfsv2; sscode=GM0MyAyOv5OeE75IGMbEjikh; GanjiUserName=%23qq_810111255; GanjiUserInfo=%7B%22user_id%22%3A810111255%2C%22email%22%3A%22%22%2C%22username%22%3A%22%23qq_810111255%22%2C%22user_name%22%3A%22%23qq_810111255%22%2C%22nickname%22%3A%22%5Cu5343%5Cu5c18%5Cu5239%22%7D; bizs=%5B%5D; GANJISESSID=hnp5af0s9a6nmui8otnkb9okbv; last_name=%23qq_810111255; xxzl_smartid=2aaafbd1c5034c1048940dbb95c302f3; Hm_lvt_655ab0c3b3fdcfa236c3971a300f3f29=1563765311; Hm_lvt_acb0293cec76b2e30e511701c9bf2390=1563765312; Hm_lpvt_655ab0c3b3fdcfa236c3971a300f3f29=1563765331; Hm_lpvt_acb0293cec76b2e30e511701c9bf2390=1563765378; __utmc=32156897; __utmz=32156897.1563765392.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A54696744669%2C%22kw%22%3A%22it%22%7D; vip_version=new; __utma=32156897.1707766422.1563765392.1563789598.1563795860.6; __utmt=1; citydomain=cd; gj_footprint=%5B%5B%22%5Cu6559%5Cu5e08%22%2C%22%5C%2Fzpjiaoshi%5C%2F%22%5D%2C%5B%22%5Cu7535%5Cu8bdd%5Cu9500%5Cu552e%22%2C%22%5C%2Fzpdianhuaxiaoshou%5C%2F%22%5D%2C%5B%22%5Cu552e%5Cu524d%5Cu5de5%5Cu7a0b%5Cu5e08%22%2C%22%5C%2Fzpsqgongchengshi%5C%2F%22%5D%5D; zhaopin_lasthistory=zpjiaoyupeixun%7Czpjiaoshi; zhaopin_historyrecords=cd%7Czpjiaoshi%7C-; Hm_lvt_acb0293cec76b2e30e511701c9bf2390=1563765312; Hm_lvt_655ab0c3b3fdcfa236c3971a300f3f29=1563765311; Hm_lpvt_655ab0c3b3fdcfa236c3971a300f3f29=1563797061; __utmb=32156897.5.10.1563795860; ganji_login_act=1563797074076; Hm_lvt_8da53a2eb543c124384f1841999dcbb8=1563797074; Hm_lpvt_8da53a2eb543c124384f1841999dcbb8=1563797074; Hm_lpvt_acb0293cec76b2e30e511701c9bf2390=1563797074',
    # 'Host': 'bj.ganji.com',
    # 'Referer': 'http://bj.ganji.com/qiuzhi/',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
}

    def parse(self, response):
        listurls = response.xpath('//div[@class="f-con-right fl js-content-container"]//div//dl//dd//a/@href').extract()
        # listurls = ['/qzdianhuaxiaoshou/', '/qzxiaoshoudaibiao/']
        for i in listurls:
            listurl1 = 'http://cd.ganji.com'+i+'o'
            for j in range(1,60):
                listurl = listurl1 + str(j)
                print('listurl', listurl)
                try:
                    yield scrapy.Request(url=listurl, callback=self.parselist, dont_filter=True, headers=self.headers)
                except:
                    pass

    def parselist(self, response):
        # time.sleep(0.2)

        code = response.xpath('//div[class="main"]/div[@class="code_img"]/span/text()').extract_first()
        print(code)
        if code == '请在五分钟内完成验证':
            exit()
        try:

            peps_info = response.xpath('//div[@class="basic-info"]')
            addr_salary = response.xpath('//div[@class="fl district-salary"]')
            for info in range(len(peps_info)):
                name = peps_info[info].xpath('.//span[1]//text()').extract_first()
                sex = peps_info[info].xpath('.//span[2]//text()').extract_first()
                age = peps_info[info].xpath('.//span[3]//text()').extract_first()
                edu = peps_info[info].xpath('.//span[4]//text()').extract_first()
                addr = addr_salary[info].xpath('.//p[@class="district"]/text()').extract_first().strip()
                salary = addr_salary[info].xpath('.//p[@class="salary"]/text()').extract_first()
                job = '/'
                dreItem = items.GanjiItem()
                dreItem['name'] = name
                dreItem['sex'] = sex
                dreItem['age'] = age
                dreItem['edu'] = edu
                dreItem['addr'] = addr
                dreItem['excjob'] = job
                dreItem['excsalary'] = salary
                yield dreItem
        except:
            pass



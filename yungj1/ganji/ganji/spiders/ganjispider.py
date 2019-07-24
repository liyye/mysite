# -*- coding: utf-8 -*-
import scrapy, time
from yungj1.ganji.ganji import items as items


class GanjispiderSpider(scrapy.Spider):
    name = 'ganjispider'
    allowed_domains = ['sh.ganji.com/qiuzhi/']
    start_urls = ['http://sh.ganji.com/qiuzhi/']
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'statistics_clientid=me; GANJISESSID=iakkh0on3e0vk6lkgt0lilgbkm; cityDomain=bj; lg=1; ganji_uuid=1418721682011074856459; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A53017876393%7D; sscode=tG7%2Bk2ELSA83cfUttGQiAi7z; GanjiUserName=daqingyizrz; GanjiUserInfo=%7B%22user_id%22%3A810100817%2C%22email%22%3A%22%22%2C%22username%22%3A%22daqingyizrz%22%2C%22user_name%22%3A%22daqingyizrz%22%2C%22nickname%22%3A%22%22%7D; bizs=%5B%5D; supercookie=BQRjZGNjBQR3WTVlAGL3AQD3ZmyxZTZkMQMwZmH1AwRjMzRjMwAvBTR0ZGx3MGZ2ZTD%3D; username_login_n=daqingyizrz; GanjiLoginType=0; ganji_xuuid=866139e2-aaa1-446d-de74-42e1f790fe1c.1563691421859; xxzl_deviceid=X33PZBRiAgPvIeO%2Fa1Ns7SHi0dMXu%2Fc5%2F4T6yt6%2FhXcthQDwrAerGsW4nUmaFXkM; xxzl_smartid=8e1d25275d5d27f29764072c0b18e2a5; Hm_lvt_acb0293cec76b2e30e511701c9bf2390=1563690784,1563690978,1563691435,1563691486; Hm_lvt_655ab0c3b3fdcfa236c3971a300f3f29=1563690796,1563691486; citydomain=bj; last_name=daqingyizrz; Hm_lvt_8da53a2eb543c124384f1841999dcbb8=1563690979,1563695790; Hm_lpvt_655ab0c3b3fdcfa236c3971a300f3f29=1563698731; Hm_lpvt_8da53a2eb543c124384f1841999dcbb8=1563699650; Hm_lpvt_acb0293cec76b2e30e511701c9bf2390=1563699650; Hm_lvt_6f6548400acfbcc44a302e67525049f7=1563699699; Hm_lpvt_6f6548400acfbcc44a302e67525049f7=1563700198; __utmt=1; __utmt_~1=1; ganji_login_act=1563700332072; __utma=32156897.1438391974.1563700332.1563700332.1563700332.1; __utmc=32156897; __utmz=32156897.1563700332.1.1.utmcsr=bj.ganji.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=32156897.1.10.1563700332; nTalk_CACHE_DATA={uid:kf_10111_ISME9754_810100817}; NTKF_T2D_CLIENTID=guest5DDBA4B6-8D26-6567-FB47-13CDA3129254; xzfzqtoken=QIYWK0LqzGjg23HQwguYHJgC93hopNvQZx3Rp%2FaET6VkcRcCgz4JhoadcB8hxTDkin35brBb%2F%2FeSODvMgkQULA%3D%3D',
    # 'Host': 'bj.ganji.com',
    # 'Referer': 'http://bj.ganji.com/qiuzhi/',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
}

    def parse(self, response):
        listurls = response.xpath('//div[@class="f-con-right fl js-content-container"]//div//dl//dd//a/@href').extract()
        # listurls = ['/qzdianhuaxiaoshou/', '/qzxiaoshoudaibiao/']
        for i in listurls:
            listurl1 = 'http://sh.ganji.com'+i+'o'
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



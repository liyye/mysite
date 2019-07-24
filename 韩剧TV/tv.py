import requests
from lxml import etree

url='https://www.hanjutv.com/hanju/7272.html'

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'cookie': '__cfduid=da38d9addbcaf9de07ed8cac37d75a1bf1563356502; Hm_lvt_06d18bf0dcdca7a8e084a650d5e8b245=1563356460; UM_distinctid=16bff4e73a23d9-0cd192640187f1-e343166-144000-16bff4e73a32a3; Hm_lpvt_06d18bf0dcdca7a8e084a650d5e8b245=1563366421',
            'Origin': 'https://ww4.hanjutv.com',
            'Referer': 'https://ww4.hanjutv.com/index.php?path=https://meiju4.qfxmj.com/20190216/vaRFOBjB/index.m3u8&f=ck_m3u8',
}

re=requests.get(url)
# print(re.text)
h=etree.HTML(re.text)
a=h.xpath('//ul[@class="juji-list clearfix"]//li/a/@href')
for i in a:
    # print('https://www.hanjutv.com'+i)
    pr='https://www.hanjutv.com'+i
    rex=requests.get(pr)
    # print(rex.text)
    h1=etree.HTML(rex.text)
    a1=h1.xpath('//*[@id="playPath"]/@src')
    # print('https:'+a1[0])
    pr1='https:'+a1[0]
    # print(pr1)
    qq=requests.get(pr1,headers=headers).content
    print(qq)



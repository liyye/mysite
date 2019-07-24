import requests
from lxml import etree
# url='http://www.epjob88.com/admincompanyNew/GzResumePreview.php?ResumeId=job10011785786819&r=62255db95637b04fce8b2467778f8eb2&uid=cm1563627377977&fromtype=gz'
from my_fake_useragent import UserAgent
a=UserAgent()
# while 1:
#     print(a.random())
p=a.random()
headers = {
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'User-Agent': p,
            # 'cookie': '__cfduid=dce1ed34975ff71acb9b22d4959d0263b1563521810; ASP.NET_SessionId=1oj0zvk0wttwcudymxjeftpt; UM_distinctid=16c0928d2b2448-03463007e150d9-e343166-144000-16c0928d2b32f6; CNZZDATA1255263807=653621382-1563520703-%7C1563520703; ViewHistory_4=1oj0zvk0wttwcudymxjeftpt; .ynzpauth=869D169A9273686FE3F281194E66EAF796DA177B8799BC0686C9AFD983575676620178F545B8CC60F7FEAA6886B258DF06E4D0E13BBE33ABBA3DCF46FB3A659EE847BBE2696F2256B15111D8D1BDD642178E9567CF7161BDEA9BC44159707D7DF2F8D7D349B8397F87AA820265CC36F284BFECA0EF6E38D76411703DA70E1B5EB03806C9211CD2EC6C800D8E4E9CC840A8734ACC7E31910E493DCF0B2D859E27; viewedResume=2088560%2C1515707%2C727002%2C1218946%2C1623681%2C2131167%2C2121066'
}
'http://www.bole.com.cn/resume/resume-show.php?id=2426'
for i in range(5786819,5786830):
    url='http://www.gzrc.com.cn/myNew/resume/ResumePreview_yl1001.php?ResumeId=job1001178'+str(i)+'&gjTag=3&SearchKey=it&readsourceflag=3&fromtype=gz&uid=cm1563627377977'

    with requests.session() as s:
        a=s.get(url,headers=headers)
        # print(a.text)
        c=etree.HTML(a.text)
        q1=c.xpath('//*[@id="mainFrame"]/@src')
        print(q1)
        # r=q1[0]
        # a1 = s.get(r, headers=headers)
        # print(a1.text)
        # r1=q1[1]
    # q1=r+r1
    # q2=c.xpath('//*[@id="main"]/div[2]/ul/li[3]/text()')[0]
    # q3=c.xpath('//*[@id="main"]/div[2]/ul/li[4]/text()[1]')[0]
    # q4=c.xpath('//*[@id="main"]/div[2]/ul/li[4]/text()[2]')[0]
    # q5=c.xpath('//*[@id="main"]/div[2]/ul/li[5]//text()')
    # e=q5[0]
    # e1=q5[1]
    # q5=e+e1
    # q6=c.xpath('//*[@id="main"]/div[2]/ul/li[6]/text()[1]')[0]
    # q7=c.xpath('//*[@id="main"]/div[2]/ul/li[6]/text()[2]')[0]
    # q8=c.xpath('//*[@id="main"]/div[2]/ul/li[8]/p/text()')[0]
    # q9=c.xpath('//*[@id="main"]/div[9]//text()')
    # q9 = [''.join([i.strip() for i in price.strip().split('\t')]) for price in q9]
    # q9 = ''.join(q9)
    # print(q1)
    # print(q2)
    # print(q3)
    # print(q4)
    # print(q5)
    # print(q6)
    # print(q7)
    # print(q8)
    # print(q9)















# import MySQLdb
# conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='papa', charset='utf8')
# cursor = conn.cursor()
# cursor.execute("select index1 from jobindex")
# a = cursor.fetchone()
# kwIndex1 = a[0]
# print(kwIndex1)

# url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=4&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format('123')
# print(url)
# url_detail = 'https://www.lagou.com/jobs/{}.html'.format('positionId')
# url_detail1 = 'https://www.lagou.com/jobs/%s.html' %'123'
#
# print(url_detail)
# print(url_detail1)

# a = ['bj', 'sh', 'gz', 'sz', 'cd', 'hz', 'nj', 'tj', 'wh', 'cq']
# for i in a:
#     for kwIndex11 in range(1, 10):
#         url = 'https://' + i + '.58.com/job/pn' + str(kwIndex11) + '/pve_5363_24'
#         print(url)


# a = ['Java', 'Python', '全栈', '爬虫', 'UI设计师', '数据分析师', '数据架构', 'wed前端', '美工', '人工智能', 'PHP', '区块链', '数据开发', '金融产品',
#          '证券', '操盘手', '信托', '权证', '交易员', '基金', '典当', '会计', '税务', '出纳', '市场推广', '销售顾问', '旅游顾问']
# c = ['530', '538', '801', '854', '635']
#
# for j in a:
#     for u in c:
#         for i in range(5):
#             params = {'start': i,'cityId': j,'kw': u,'kt': 3}
#             print(params)

# for i in range(1):
#     start_urls = ['https://fe-api.zhaopin.com/c/i/sou?start=' + str(i * 90) + '&pag']
#     print(start_urls)

# if '月' not in 'qr月rwr':
#     print('当前时间')
# else:
#     print('原来时间')
#
# # a=''+'12'+''
# # print(a)
#
# S = 'abcdefghijklmnop'
# a=S[::1]
# print(a)
# import time
# def qq():
#     print('111')
#     time.sleep(0.3)
#     qq()
# qq()

# for i in range(11147):
#     url = 'https://cx.ht.cn/home-index-comsearch-m-Home-skey-d2b58408c720b00b76da91b64c8af894-p-' + list(i) + '.html'
#     print(url)
    # yield scrapy.Request(url=url, callback=self.parListPage, dont_filter=True)

a='意向岗位:'
b='养殖部主管'
c=a+b
print(c)
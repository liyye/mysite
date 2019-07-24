import bs4
import requests, json, time



def run():
    """***************************遍历页码*********************************"""
    for i in range(1, 31):
        """
         第一个请求对象
        """
        ses = requests.Session()

        job_name = "python"
        city = "北京"
        doc_url = "https://www.lagou.com/jobs/list_{job_name}".format(job_name=job_name)
        ses.headers[
            "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
        ses.headers["Host"] = "www.lagou.com"

        doc_response = ses.get(url=doc_url, params={"city": city})

        ajax_headers = {
            "Origin": "https://www.lagou.com",
            "Referer": 'https://www.lagou.com/jobs/list_python?px=default&city=%E5%8C%97%E4%BA%AC',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
        }

        ajax_url = "https://www.lagou.com/jobs/positionAjax.json?=false"


        data = {
            "first": "false",
            "pn": i,
            "kd": "python"
        }

        ajax_response = ses.post(url=ajax_url,
                                 params={"needAddtionalResult": "false", "city": city},
                                 data=data,
                                 headers=ajax_headers,
                                 timeout=3)


        if ajax_response.status_code == 200:
            info_dic = ajax_response.json()

            lists = info_dic['content']['positionResult']['result']


            """***************************遍历json串*********************************"""
            for i in lists:
                # print(i) #  'positionId': 6127709
                positionId = i.get('positionId')
                # print(positionId) # 6127709

                headers ={
                    'Referer':'https://www.lagou.com/jobs/list_python?px=default&city=%E5%8C%97%E4%BA%AC',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
                }

                url_detail = 'https://www.lagou.com/jobs/{}.html'.format(positionId)

                """
                第二个请求对象
                """
                ses2 = requests.Session()
                res = ses2.get(url_detail,timeout=3,headers=headers)
                # cookies = ses2.cookies

                res = ses2.get(url_detail, timeout=3,headers=headers)
                print('***************************************')
                # print(res.text)
                soup = bs4.BeautifulSoup(res.text, 'lxml')
                duty = soup.find_all(class_="job_detail")[0].get_text().replace(' ', '').replace('\n','')
                print(duty)# 详情页的职责
                print('***************************************')

                # positionName = i.get('positionName')
                # salary = i.get('salary')
                # workYear = '经验'+ i.get('workYear')
                # edccation = i.get('education') + '以上'
                # jobNature = i.get('jobNature')
                # positionLables = i.get('positionLables')
                # companyLabelList = i.get('companyLabelList')
                # companyShortName = i.get('companyShortName')
                # financeStage = i.get('financeStage')
                # financeStage = i.get('industryField')
                print('这是路径:',url_detail)
                print("准备保存数据")
                print()
                # # break
                # time.sleep(3)


if __name__ == '__main__':
    run()


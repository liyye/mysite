import requests
import time
import random

#获取网页原数据
def get_json(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    params={
        'page_size':'10',
        'next_offset':str(num),
        'tag':'今日热门',
        'platform':'pc',
    }
    try:
        html=requests.get(url,headers=headers,params=params)
        return html.json()
    except:
        print("请求错误")
        pass

#下载视频
def downloader(url,path):
    start=time.time()#开始时间
    size=0
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    response=requests.get(url,headers,stream=True)#stream属性必须带上
    chunk_size=1024#每次下载的数据大小
    content_size=int(response.headers['content-length'])#总大小
    if response.status_code==200:
        print('[文件大小]：%0.2fMB'%(content_size/chunk_size/1024))#换算单位
        with open(path,'wb')as f:
            for data in response.iter_content(chunk_size=chunk_size):
                f.write(data)
                size+=len(data)

if __name__ == '__main__':
    for i in range(10):
        url='http://api.vc.bilibili.com/board/v1/ranking/top?'
        num=i*10+1
        html=get_json(url)
        infos=html['data']['items']
        for info in infos:
            title=info['item']['description']#小视频的标题
            video_url=info['item']['video_playurl']#视频地址
            print(title,video_url)
            #为了防止视频没有video_url
            try:
                downloader(video_url,path="%s.mp4"%title)
                print("成功下载一个")
            except BaseException:
                print("下载失败")
                pass
        time.sleep(int(format(random.randint(2,8))))#设置随机等待时间

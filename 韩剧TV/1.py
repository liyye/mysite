# -*-coding:utf-8-*-
import sys
import you_get
def download(url, path):
    sys.argv = ['you-get', '-o', path, url]
    you_get.main()
if __name__ == '__main__':
    # 视频网站的地址
    url = 'https://www.bilibili.com/video/av6117110?from=search&seid=71809532639914617'
    # 视频输出的位置
    path = 'E:/test'
    download(url, path)


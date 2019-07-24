# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial' # 爬虫名称 U-A 默认是BOT_NAME

SPIDER_MODULES = ['tutorial.spiders']  # spider的名字
NEWSPIDER_MODULE = 'tutorial.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # 君子协定

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True  # 是否启用cookie

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
  'Cookie': 'f=n; commontopbar_new_city_info=1%7C%E5%8C%97%E4%BA%AC%7Cbj; userid360_xml=C8D2A546F12E14C113F68232E1D34D8E; time_create=1565233536109; f=n; id58=e87rZl0YaLe3DNz1DW6yAg==; als=0; wmda_uuid=7168794239d45fe61b7a79d8a3c623f6; wmda_new_uuid=1; wmda_visited_projects=%3B1731916484865; bProtectShowed=true; cookieuid1=e87rjV0kC82jv/YSAw/ZAg==; Hm_lvt_5a7a7bfd6e7dfd9438b9023d5a6a4a96=1562643367; commontopbar_ipcity=bj%7C%E5%8C%97%E4%BA%AC%7C0; jobBottomBar=1; sessionid=1eb695d3-2f30-4a72-ad9f-095c2a8e9388; gr_user_id=386265c0-f7b1-4d30-9ee1-a44e0da6eba2; Hm_lvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1562641563,1562763043; Hm_lpvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1562763341; ppStore_fingerprint=21B7C47E802F57D5EC72654E35E89D50E2A5EA8C2281E2D2%EF%BC%BF1562763341940; mcity=bj; 58home=bj; f=n; commontopbar_new_city_info=1%7C%E5%8C%97%E4%BA%AC%7Cbj; city=bj; JSESSIONID=CBA6B0239FF4F4166CCDCAFFAF958DE7; 58tj_uuid=c201a52e-b5dd-4362-b696-ebf22eb754a9; new_session=0; new_uv=3; utm_source=market; spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT; init_refer=; Hm_lvt_5bcc464efd3454091cf2095d3515ea05=1562641536,1562762717; Hm_lpvt_5bcc464efd3454091cf2095d3515ea05=1562765105; xxzl_deviceid=0OX8Kw%2FL5GOKGZoDczZ2FXwOtOGgFFtAcPEI0Owwsle2azudyphz7TEvDv6F5FZT; wmda_session_id_1731916484865=1562762701449-ec07da44-f4ab-87e5',

}

# Enable or disable spider middlewares  # 设置启用中间件
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialDownloaderMiddleware': 543,
#}

########################################################

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'tutorial.pipelines.TutorialPipeline': 320,  # 入库  300表示权重 决定顺序
   'tutorial.pipelines.DropPipeline': 310,  # 去重
   'tutorial.pipelines.CleanPipeline': 311,  # 清洗
   'tutorial.pipelines.DatePipeline': 315,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

HOST='localhost'
PORT=3306
USER='root'
PASSWORD='123'
DB='papa'
CHARSET='utf8'


JOB_DIR='hehe.txt' # 自动设置断点记录  注意：多个spider之间不共享





















# -*- coding: utf-8 -*-

# Scrapy settings for ganji project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ganji'

SPIDER_MODULES = ['ganji.spiders']
NEWSPIDER_MODULE = 'ganji.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Cookie': "statistics_clientid=me; ganji_uuid=3983696531279761349146; ganji_xuuid=95ecf234-7501-4684-82b9-863b4ce41102.1563693096421; cityDomain=bj; _wap__utmganji_wap_newCaInfo_V2=%7B%22ca_n%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_i%22%3A%22-%22%7D; lg=1; WantedListPageScreenType=1536; STA_DS=1; citydomain=bj; Hm_lvt_acb0293cec76b2e30e511701c9bf2390=1563694652; xxzl_deviceid=D6o0VTsWEVcj3%2BUo48CH4D1qABUOnMJzA3PX9FaL3qCLliEl8JZIk3QPqH0bfsv2; sscode=GM0MyAyOv5OeE75IGMbEjikh; GanjiUserName=%23qq_810111255; GanjiUserInfo=%7B%22user_id%22%3A810111255%2C%22email%22%3A%22%22%2C%22username%22%3A%22%23qq_810111255%22%2C%22user_name%22%3A%22%23qq_810111255%22%2C%22nickname%22%3A%22%5Cu5343%5Cu5c18%5Cu5239%22%7D; bizs=%5B%5D; GANJISESSID=hnp5af0s9a6nmui8otnkb9okbv; last_name=%23qq_810111255; Hm_lvt_655ab0c3b3fdcfa236c3971a300f3f29=1563764270; xxzl_smartid=2aaafbd1c5034c1048940dbb95c302f3; Hm_lvt_8da53a2eb543c124384f1841999dcbb8=1563764319; Hm_lvt_6f6548400acfbcc44a302e67525049f7=1563764843; Hm_lpvt_6f6548400acfbcc44a302e67525049f7=1563764843; Hm_lvt_655ab0c3b3fdcfa236c3971a300f3f29=1563765311; Hm_lvt_acb0293cec76b2e30e511701c9bf2390=1563765312; Hm_lpvt_655ab0c3b3fdcfa236c3971a300f3f29=1563765331; Hm_lpvt_acb0293cec76b2e30e511701c9bf2390=1563765378; __utmc=32156897; __utmz=32156897.1563765392.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); gj_footprint=%5B%5B%22%5Cu7535%5Cu8bdd%5Cu9500%5Cu552e%22%2C%22%5C%2Fzpdianhuaxiaoshou%5C%2F%22%5D%2C%5B%22%5Cu552e%5Cu524d%5Cu5de5%5Cu7a0b%5Cu5e08%22%2C%22%5C%2Fzpsqgongchengshi%5C%2F%22%5D%5D; zhaopin_lasthistory=zpshichangyingxiao%7Czpdianhuaxiaoshou; zhaopin_historyrecords=bj%7Czpdianhuaxiaoshou%7C-%2Cbj%7Czpsqgongchengshi%7C-; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A54696744669%2C%22kw%22%3A%22it%22%7D; SiftRecord['1563765544']=it%3C%E6%B1%82%E8%81%8C%E7%AE%80%E5%8E%86%3E%7C%7C%2Fqiuzhi%2Fs%2F_it%2F%3Ffrom%3Dzhaopin_indexpage; vip_version=new; Hm_lpvt_655ab0c3b3fdcfa236c3971a300f3f29=1563767076; __utma=32156897.1707766422.1563765392.1563765392.1563776500.2; Hm_lpvt_8da53a2eb543c124384f1841999dcbb8=1563777119; Hm_lpvt_acb0293cec76b2e30e511701c9bf2390=1563777120",
'Host': 'bj.ganji.com',
'Upgrade-Insecure-Requests': 1

}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ganji.middlewares.GanjiSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'ganji.middlewares.GanjiDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'ganji.pipelines.GanjiPipeline': 300,
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
LOG_LEVEL = 'INFO'
JOB_DIR = 'duandian'

HTTPERROR_ALLOWED_CODES = [404]
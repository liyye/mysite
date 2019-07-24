# -*- coding: utf-8 -*-

# Scrapy settings for zhill project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhill'

SPIDER_MODULES = ['zhill.spiders']
NEWSPIDER_MODULE = 'zhill.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhill (+http://www.yourdomain.com)'
USER_AGENTS=[{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'},
             {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
             {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'},
             {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50'},
             {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)'},
             {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E) QQBrowser/6.9.11079.201'},
             ]


# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # 君子协定

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False  # 是否启用cookie

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'cookie': 'x-zp-client-id=dc697fa9-7489-4f99-b1be-7448c8b68985; sts_deviceid=16be5f1b073372-00dc0e6f644222-e343166-1327104-16be5f1b0745d8; adfbid2=0; sou_experiment=psapi; ZP_OLD_FLAG=false; acw_tc=2760827315629322531866501eab0949567a1cd0818cf105c128f52b46e668; _jzqx=1.1562936167.1562939263.1.jzqsr=jobs%2Ezhaopin%2Ecom|jzqct=/.-; dywez=95841923.1562994877.4.2.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1562931831,1562994877; __utmz=269921210.1562994878.4.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216be5f20b6ae8-0455199e7a68ad-e343166-1327104-16be5f20b6b3ce%22%2C%22%24device_id%22%3A%2216be5f20b6ae8-0455199e7a68ad-e343166-1327104-16be5f20b6b3ce%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; LastCity=%E5%85%A8%E5%9B%BD; LastCity%5Fid=489; urlfrom2=121126445; adfcid2=none; _qzja=1.871204292.1562936166991.1563003209297.1563008039198.1563004350641.1563008039198.0.0.0.5.4; _qzjto=3.2.0; _jzqa=1.930816075143718800.1562936167.1563003209.1563008039.4; _uab_collina=156300953480012330339195; __utma=269921210.326282386.1562930966.1563008039.1563010721.7; dywea=95841923.1186125370086396700.1562930967.1563008039.1563010721.7; smidV2=2019071317384112f6f9faf2cd450217263f921e54461e00bb02164653bb7d0; sts_sg=1; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fjobs.zhaopin.com%2FCZ713161080J00329233805.htm; jobRiskWarning=true; acw_sc__=5d29d524c802105e75166f255068e69fca30151a; ZL_REPORT_GLOBAL={%22jobs%22:{%22recommandActionidShare%22:%22427e8866-9edc-4ba1-95e0-8f8d7d0179b0-job%22%2C%22funczoneShare%22:%22dtl_best_for_you%22}}; sts_evtseq=1; sts_sid=16beb68157f40b-0a3923c3511e76-e343166-1327104-16beb681580574'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhill.middlewares.ZhillSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'zhill.middlewares.UADownloaderMiddleware': 543,
   # 'zhill.middlewares.ProxyDownloaderMiddleware': 544,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zhill.pipelines.ZhillPipeline': 320,
   'zhill.pipelines.DropPipeline': 310,  # 去重
   'zhill.pipelines.CleanPipeline': 311,  # 清洗
   'zhill.pipelines.DatePipeline': 315,
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



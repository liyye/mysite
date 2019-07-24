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
  # 'cookie': 'Hm_lvt_55d3982f9d41b99f56a44ddcd44b78be=1563269921; SPRING_SECURITY_REMEMBER_ME_COOKIE=MTUyMzA4NzQyOTk6MTU2NDQ3OTg4ODIyNDpkZWNlODAwZjI4NmViNDcwMzU5MjQwNzVhMmUxN2QyMA; JSESSIONID=AF0B69DD7AD457691108B1CD2732D067; Hm_lpvt_55d3982f9d41b99f56a44ddcd44b78be=1563274266'
  'cookie': '__cfduid=dce1ed34975ff71acb9b22d4959d0263b1563521810; UM_distinctid=16c0928d2b2448-03463007e150d9-e343166-144000-16c0928d2b32f6; ASP.NET_SessionId=iwhh51rxx2gz4lnyad4dvj0u; ViewHistory_1=iwhh51rxx2gz4lnyad4dvj0u; CNZZDATA1255263807=653621382-1563520703-%7C1563840471; ViewHistory_4=iwhh51rxx2gz4lnyad4dvj0u; .ynzpauth=01354BE1E685AB5B71BB3298E7D3E6F1CDA71DC69C703641CFF093AACC7188733E314277DBA76CC43E2BD4CFEA2E1C327A6DC205F784E857316377CE368FC970D5D41951626C6870400580C9D7FC593EC731435C65EA959FE43C6F5A3526E86DF9EAB668EE2D997636276CD0824A196B39DF38D0CCD701D9192A64288167607599F5AFC95655588BC4A1A94FB8085D48DA2C407AE8322C5BC63204F4766AF9C9; viewedResume=2088560%2C1515707%2C727002%2C1218946%2C1623681%2C2131167%2C2121066%2C1966094%2C2125187%2C1951642%2C2131775%2C2130856%2C1932086%2C1796864%2C1653051'

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
   # 'zhill.pipelines.CleanPipeline': 311,  # 清洗
   # 'zhill.pipelines.DatePipeline': 315,
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
DB='yunyun'
CHARSET='utf8'

JOB_DIR='hehe.txt' # 自动设置断点记录  注意：多个spider之间不共享



BOT_NAME = 'index'

SPIDER_MODULES = ['index.code']
NEWSPIDER_MODULE = 'index.code'
# 爬取的默认User-Agent，除非被覆盖。
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

# 是否遵循robots协议，一般不要遵循设为False即可，robots.txt
ROBOTSTXT_OBEY = False


# 下载器最大并发数，默认16个
CONCURRENT_REQUESTS = 30



DOWNLOADER_MIDDLEWARES = {
   'middlewares.process_request': 541
}

# 设置管道优先级
ITEM_PIPELINES = {
   'pipelines.Pipeline': 300,
}
HTTPERROR_ALLOWED_CODES = [403]



#下载延迟
#实际是一个范围随机值： 0.5倍-1.5倍 单位秒DOWNLOAD_DELAY = 3
#若不设置随机值，设置如下：RANDOMIZE_DOWNLOAD_DELAY = False
#DOWNLOAD_DELAY = 3



# 每个域名最大并发数，默认8个
#CONCURRENT_REQUESTS_PER_DOMAIN = 100


#每个ip的最大并发数，默认0，代表没有限制
#CONCURRENT_REQUESTS_PER_IP = 100



# 是否禁用cookies
# 禁用后速度会快些，但可能会反爬，视情况而定COOKIES_ENABLED = False #禁用cookies
#COOKIES_ENABLED = False



# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

#默认请求头
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}




# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'xmeta.middlewares.XmetaSpiderMiddleware': 543,
#}


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
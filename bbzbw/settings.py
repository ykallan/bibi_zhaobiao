# Scrapy settings for bbzbw project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bbzbw'

SPIDER_MODULES = ['bbzbw.spiders']
NEWSPIDER_MODULE = 'bbzbw.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bbzbw (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'Host': 'www.bibenet.com',
  'Referer': 'https://www.bibenet.com/database/toOwnerListPage.htm?pageNum=4&pageSize=&type=1&type=1&type=1',
  'Connection': 'keep-alive',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
  'Cookie': 'Hm_lvt_72debff28530b8444ed66fb29b59be17=1597999111; UM_distinctid=174102b5d02ae3-0cd97b99da3b69-3323766-1fa400-174102b5d03ad9; Qs_lvt_272444=1597999111; index_layerAdv=113.44.149.232; uuidUV=130bb00ed7dd492ab196f800287a8339; historyUV=2020-08-21T16%3A38%3A33.043%2B08%3A00; mediav=%7B%22eid%22%3A%22570152%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22%22%2C%22ctn%22%3A%22%22%2C%22vvid%22%3A%22%22%2C%22_mvnf%22%3A1%7D; nb-referrer-hostname=www.bibenet.com; JSESSIONID=9EC3B869405D5B220E3BAB72B9E693DF; Qs_pv_272444=3883204168876829700%2C1253655791537503500%2C1578746528207361300%2C1989866125495969500%2C1731225993222481400; nb-start-page-url=https%3A%2F%2Fwww.bibenet.com%2Fdatabase%2FtoOwnerListPage.htm%26pageNum%3D1241%26pageSize%3D%26type%3D1%26%3BJSESSIONID%3D3D3F41422862F4340E57D87C5EA499E6%3Fticket%3DST-43039-wqxXbS0xEoPPrNe7nT4u-cas01.example.org; CNZZDATA1261799122=526672187-1597993723-%7C1598016232; Hm_lpvt_72debff28530b8444ed66fb29b59be17=1598016303',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'bbzbw.middlewares.BbzbwSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'bbzbw.middlewares.BbzbwDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'bbzbw.pipelines.BbzbwPipeline': 300,
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

# -*- coding: utf-8 -*-

# Scrapy settings for music project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
import string



BOT_NAME = 'music'

SPIDER_MODULES = ['music.spiders']
NEWSPIDER_MODULE = 'music.spiders'

MONGO_URI = 'localhost'
MONGO_DB = 'music'



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'music (+http://www.yourdomain.com)'

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
     'Host': 'music.163.com',
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
     'Content-Type': 'application/x-www-form-urlencoded',
     'Accept': '*/*',
     'Accept-Encoding': 'gzip, deflate',
     'Accept-Language': 'zh-CN,zh;q=0.8',
     'Cookie': 'UM_distinctid=1676a89b4fe537-0ff0904256e16a-424e0b28-100200-1676a89b4ff3d7; _ntes_nnid=0707fdce58d6fa4e8078d6d9a583b60d,1543680670183; _ntes_nuid=0707fdce58d6fa4e8078d6d9a583b60d; vjuids=-4b501a074.16787038a1c.0.25504438a6abb; __gads=ID=22e3e6bd8279b4bc:T=1544158458:S=ALNI_MZeny-Lbyg-vFj83WWYbvSyyRcMbQ; mail_psc_fingerprint=d15e36edce01e9418b6069626ec480f9; usertrack=CrHualwKHhhox69cAwOFAg==; _iuqxldmzr_=32; WM_TID=tP3Ly924BQNEUAUAQRd4LpUqxHaT69R9; NTES_CMT_USER_INFO=267149387%7C%E6%9C%89%E6%80%81%E5%BA%A6%E7%BD%91%E5%8F%8B0fX61b%7C%7Cfalse%7CbTE4NDM0MzY2Njg5XzJAMTYzLmNvbQ%3D%3D; vinfo_n_f_l_n3=f1c3b4de809e2522.1.3.1544158455097.1544331925980.1544794236300; __f_=1544846628500; vjlast=1544158415.1544859987.11; P_INFO=m18434366689_2@163.com|1545134617|0|other|00&99|hun&1544504137&other#hun&430100#10#0#0|184689&1||18434366689@163.com; c98xpt_=30; jsessionid-cpta=lKHHgtvmib%2BlDVIeX8M9nr%2BX84kKEAmmi6%2B3GiFRuoHUGul1eYy8FkUaDQCz4UcTFjuWutKlfNIbhXvGe0xpTAyc4uYtvB9l2fvCGS%2BrTtfHQpXvybYgF7efPXFOKDp%2B%5C1bZ0u%2F36OQZjh8%5CULpw5XtEoHK1TBJZT%2Bwf%2FzLHM0CXRd8O%3A1545215135458; __remember_me=true; __utmc=94650624; WM_NI=UvtJXjPEowONYY9zBhJRDpnaAKlSxNJJQlrauZY0teX5Tt55EfAr1kUxNxwknOIhY0KsKcTBXVICHrEO8qOr1k%2FQ3R5P7DoAEld5vWWXcuJEfOviqOr2JZZKdZ7T5DvwaUI%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee90fc549a89a1b4fc6aa7968fa6d54f828b9aaef241f5babbb8c73bbabc86b5eb2af0fea7c3b92a97aabcabdb62949ba198ce469b87f79bc1648a8e8c91ed6b8395a4b4fb468a969f8df16bb78697d1f76f9ceb9c95b83f87ba8f93b46197a88299f661ae918789dc3c89ad8584d74a9c8a87a4cb7a8791f892ce7af3b5e1b2b25af790f9a5ee4b87b4acd6f55d9588ad96c94fa691ba8af445b2ee86bbd941a886f9b5b850b6a9afb6cc37e2a3; JSESSIONID-WYYY=pbYJy6uRThpTRp0TrsKS2bre761VC2JTP4%2FXMqzjKaOODoin9RyTxsAJeMquNHT%5C9RmsdDcRSlUq3QfkKXE4GrfGAJ9vM2aviOpj%5ClUNT8D4Yskoh%2FP2cQ0%5C4GQSGvyTvA0OKg7OQvx%2FrpGlTCM23MAnJDkaOItvENSmnPqhU%2BK7BoyT%3A1545651071216; __utma=94650624.309877944.1544932288.1545639714.1545649795.19; __utmz=94650624.1545649795.19.13.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; MUSIC_U=ca7afb5bc429ac112d1629bfd9667f671ba51a2d735dbd944198e22870452d05ae52f69889250f52f12503c57c420cc831b299d667364ed3; __csrf=6bc3a846421eed6408c8d72e1d48ac0e; __utmb=94650624.6.10.1545649795'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'music.middlewares.MusicSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#    'music.middlewares.MusicDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
   # 'music.middlewares.MusicDownloaderMiddleware':543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
#    'music.pipelines.MusicPipeline': 300,
    'music.pipelines.MongoPineline': 400,
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

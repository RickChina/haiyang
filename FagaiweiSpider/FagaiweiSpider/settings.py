# -*- coding: utf-8 -*-

import MySQLdb.cursors
import datetime

# Scrapy settings for FagaiweiSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'FagaiweiSpider'

SPIDER_MODULES = ['FagaiweiSpider.spiders']
NEWSPIDER_MODULE = 'FagaiweiSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent


# Obey robots.txt rules
#ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'FagaiweiSpider.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#    'FagaiweiSpider.middlewares.MyCustomDownloaderMiddleware': 543,
    "FagaiweiSpider.middlewares.UserAgent":543,
    "FagaiweiSpider.middlewares.IngoreRequestMiddleware":540,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    #"FagaiweiSpider.pipelines.FilesPipeline":1,
    'FagaiweiSpider.pipelines.FagaiweispiderPipeline': 300,
    'FagaiweiSpider.pipelines.InsertRideis': 100,
    'FagaiweiSpider.pipelines.InsertPDFpath': 200,
    #'FagaiweiSpider.pipelines.PDFPipeline': 200,
    #"FagaiweiSpider.pipelines.ShuilibuspiderPipeline": 302,
}
FILES_STORE = "D:\\Mycode\\FagaiweiSpider\\images"
WRITE_DATE = {
    "host":"192.168.58.129",
    "user":"root",
    "passwd":"mysql",
    "db":"test2",
    "charset":"utf8",
    "use_unicode":True,
    "cursorclass":MySQLdb.cursors.DictCursor
}
LOG_FILE = "logs\\\\%shy.log" % datetime.datetime.now().strftime("%Y-%m-%d")
# LOG_LEVEL = "ERROR"
LOG_LEVEL = "INFO"

#JOBDIR='sharejs.com'

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

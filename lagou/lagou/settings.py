# -*- coding: utf-8 -*-

# Scrapy settings for lagou project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lagou'

SPIDER_MODULES = ['lagou.spiders']
NEWSPIDER_MODULE = 'lagou.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lagou (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Cache-Control":"no-cache",
    "Connection":"keep-alive",
    "Host":"www.lagou.com",
    "Pragma":"no-cache",
    "Cookie":'user_trace_token=20180120212822-c98c62b1-fde5-11e7-b08c-525400f775ce; LGUID=20180120212822-c98c689d-fde5-11e7-b08c-525400f775ce; index_location_city=%E5%8C%97%E4%BA%AC; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1517626975,1517630016,1517638248,1517793412; _gat=1; _gid=GA1.2.227984683.1517793412; LGSID=20180205091655-4144ddcd-0a12-11e8-af69-5254005c3644; PRE_UTM=m_cf_cpc_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.Kf0000jA5uApXoP2P8KYkR-8rOm0FgioZ2s9-UtoAFWN-luM55IHGmnYtmAuqCB7jipe1wW2ay8GMhqYgzp4mxD38Xh_7Gfzwikos6k8c0AhIiclIy6Jx8nm6NXyytMLxTdTQg_PZj-7MNGwADiLnrfKBIuefaEsDr5QQg-nB6e6wE-Cqf.DR_NR2Ar5Od663rj6tJQrGvKD7ZZKNfYYmcgpIQC8xxKfYt_U_DY2yP5Qjo4mTT5QX1BsT8rZoG4XL6mEukmryZZjzt5jzGoo_deSgFYebdlSgj4qrZul3IhOj4etrOF9q8qmhPOHvUo2OZk4mSyG-LQWdQjPakEoLI260.U1Yk0ZDqs2v4_sK9uZ745TaV8Un0mywkIjYz0ZKGm1Yk0Zfqs2v4_sKGUHYznWR0u1dCugK1nfKdpHdBmy-bIykV0ZKGujYkP0KWpyfqn1cz0AdY5HDsnHIxnH0krNt1nHnvg1DsnWPxn1msnfKopHYs0ZFY5Hm4PsK-pyfq0AFG5HcsP0KVm1YLnHT3P1DzPj-xP1DLrjTknWmkg1DdP-tkg100TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjY3nWn1P1n1rjT0UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0ZwdT1YknjTznHTvrH6dn101n1m1nWcsPfKzug7Y5HDdnHTLrHnYnHDznjm0Tv-b5yFWnhDkrjcvnj0sPHwWmWf0mLPV5RnsfHTdrDfvrjw7nj0LwjR0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7tsg100uA78IyF-gLK_my4GuZnqn7tsg1Kxn7ts0ZK9I7qhUA7M5H00uAPGujYzPW6Yn1RYPHm0ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYkP6KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KWThnqnHnd%26ck%3D4250.1.47.264.144.264.144.4%26shh%3Dwww.baidu.com%26sht%3D96450177_s_hao_pg%26us%3D1.0.1.0.0.0.0%26ie%3Dutf-8%26f%3D8%26srcqid%3D1734839470948722762%26tn%3D96450177_s_hao_pg%26wd%3D%25E6%258B%2589%25E9%2592%25A9%26oq%3D%25E6%258B%2589%25E9%2592%25A9%26rqlang%3Dcn%26sc%3DUWY4PWfdnjDLPdq1gv99UdqsuzuY5HDdnHTLrHc3P1bLPHnhm1dCmytknWnhmynqnHczP1f4nHn3P0%26ssl_sample%3Ds_51%252Cs_55%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpc_baidu_pc%26m_kw%3Dbaidu_cpc_zz_e110f9_265e1f_%25E6%258B%2589%25E9%2592%25A9; _putrc=A854A48E25B5FAE3; JSESSIONID=ABAAABAAAGFABEFCC20D98600FBFD859ADE83F80F696D0C; login=true; unick=jacob; gate_login_token=b75bc18226516d1c545163470b658c412fac521984fb8104; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1517793417; LGRID=20180205091700-44057e7b-0a12-11e8-ba2b-525400f775ce',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    "Upgrade-Insecure-Requests":1,
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lagou.middlewares.LagouSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'lagou.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'lagou.pipelines.LagouPipeline': 300,
}

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
# Count = 1
# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#encoding=utf-8
'''
这是多个爬虫同时执行的脚本文件，用apscheduler做了阻塞定时，
这个在Windows下没有测试，暂时没有使用。用的是ProceRun脚本。
'''

# from apscheduler.schedulers.twisted import TwistedScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
#from apscheduler.schedulers.background import BackgroundScheduler
import os
import datetime
import pdf_down
import logging
logging.basicConfig()

print("定时器开始执行... %s") % datetime.datetime.now().isoformat()
def my_job():
    os.chdir("/root/workspace/Myspider/FagaiweiSpider")
    print("开始执行：fagaiwei_fabu")
    os.system('scrapy crawl fagaiwei_fabu')
    print("开始执行：shui_baogao")
    os.system('scrapy crawl shui_baogao')
    print("开始执行：shuilibu")
    os.system('scrapy crawl shuilibu')
    print("开始执行：guotu_fagui")
    os.system('scrapy crawl guotu_fagui')
    print("开始执行：guotu_lanmu")
    os.system('scrapy crawl guotu_lanmu')
    print("开始执行：guotu_qita")
    os.system('scrapy crawl guotu_qita')
    print("开始执行：guotu_xiazai")
    os.system('scrapy crawl guotu_xiazai')
    print("开始执行：huanbao_falv")
    os.system('scrapy crawl huanbao_falv')
    print("开始执行：nong_gongwen")
    os.system('scrapy crawl nong_gongwen')
    print("开始执行：nong_zhengce")
    os.system('scrapy crawl nong_zhengce')
    print("爬虫结束！%s") % datetime.datetime.now().isoformat()
    pdf_down.pdf_down()

if __name__ == "__main__":
#    sched = BackgroundScheduler()
    sched = BlockingScheduler()
    sched.add_job(my_job, "cron", hour="0", minute="15")
    sched.start()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
同时运行多个爬虫的命令脚本。在Windows下添加到定时任务中即可使用。
'''

import os
os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'FagaiweiSpider.settings')
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import time
import pdf_down
import My_email

def start_project():
    process = CrawlerProcess(get_project_settings())
# 指定多个spider
#     process.crawl("fagaiwei_fabu")
#     process.crawl("shui_baogao")
    process.crawl("shuilibu")
#     process.crawl("guotu_fagui")
#     process.crawl("guotu_lanmu")
#     process.crawl("guotu_qita")
#     process.crawl("guotu_xiazai")
#     process.crawl("huanbao_falv")
#     process.crawl("nong_gongwen")
#     process.crawl("nong_zhengce")

# 执行所有 spider
    #for spider_name in process.spider_loader.list():
        #print("爬虫已经启动")
        #process.crawl(spider_name)
    process.start()
    print("爬虫结束")
    #pdf_down.pdf_down() #下载附件
    #My_email.mail()  #发邮件

if __name__ == "__main__":
    start_project()
    

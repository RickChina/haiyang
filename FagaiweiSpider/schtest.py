#coding=utf-8

'''用来测试apscheduler定时任务模块在Windows环境下运行情况'''

from apscheduler.schedulers.background import BackgroundScheduler
import os
import time

def my_job():
    with open("111.txt","a") as files:
        files.write("%s" % time.time())
backtast = BackgroundScheduler()
backtast.add_job(my_job, "interval", seconds=5)
backtast.start()

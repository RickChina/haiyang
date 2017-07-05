#encoding=utf-8

'''
国家海洋项目的PDF附件下载模块。
scrapy抓取到附件url，存入redis数据库，把文件名用绝对地址表示为key，以附件网址为value。
用urllib2模块下载。
'''

import urllib2
import redis
import os
import time
import re

def pdf_down():
    print("开始下载附件：") 
    r = redis.StrictRedis(host="localhost", port=6379, db=2)
    path_list = r.keys()
    for i in range(len(path_list)):
        pdf_path = path_list[i]
        pdf_path = re.sub(r"/home", "/root/workspace", pdf_path)
        #windows 下路径表示方式不同,用\\替换/ 。
        pdf_path = re.sub(r"/", "\\\\", pdf_path)
        if os.path.exists(pdf_path):
            continue
        elif pdf_path.startswith("delete"):
            continue
        else:
            time.sleep(1.5)
            with open(pdf_path, "wb") as fb:
                print("第%s个, key值：%s" %(i,pdf_path))
                pdf_url = r.get(path_list[i])
                req = urllib2.Request(pdf_url)
                req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
                try:
                    conn = urllib2.urlopen(req)
                    print("开始下载：%s" % pdf_url)
                    done = 0
                    while not done:
                        date = conn.readline()
                        if date != "":
                            fb.write(date)
                        else:
                            done = 1
                except Exception as e:
                    print("DownError:%s")%e
                    r.delete(path_list[i])
                    r.set("delete-%s"%path_list[i], "%s"%pdf_url)
                    return pdf_down()

    print("附件下载完成！")

if __name__ == "__main__":
    pdf_down()
    print("下载完成！")

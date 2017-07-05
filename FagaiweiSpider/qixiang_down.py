#coding=utf-8

import MySQLdb
import urllib2
import re
import os

def down(url,name):
    if name.endswith("txt"):
        files_name = "/root/workspace/Mytools/doc/%s" % name
        if not os.path.exists(files_name):
            files = open(files_name,"w")
            req = urllib2.Request(url)
            print("downing:%s" % name)
            req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
            try:
                conn_text = urllib2.urlopen(req)
                done = 0
                while not done:
                    date = conn_text.readline()
                    if date != "":
                        files.write(date)
                    else:
                        done = 1
            except Exception as e:
                print("DownError:%s")%e
            files.close()

    else:
        files_name = "/root/workspace/Mytools/doc/zip/%s" % name
        if not os.path.exists(files_name):
            files = open(files_name,"w")
            req = urllib2.Request(url)
            print("downing:%s" % name)
            req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
            try:
                conn_text = urllib2.urlopen(req)
                done = 0
                while not done:
                    date = conn_text.readline()
                    if date != "":
                        files.write(date)
                    else:
                        done = 1
            except Exception as e:
                print("DownError:%s")%e
            files.close()


try:
    conn = MySQLdb.connect(
        host="120.76.242.206", port=3306, db="caiji_shs", user="cnki5631",
        passwd="cnkipassword5631", charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("select url from weather")
    result = cur.fetchall()
    for i in result:
        url = i[0]
        #print(url)
        name = re.findall(r"(S\d+\.\D+)\?",url)[0]
        down(url, name)
    cur.close()
    conn.close()


except Exception, e:
    print e.message

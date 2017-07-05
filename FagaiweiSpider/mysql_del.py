#coding=utf-8

'''
用MySQLdb模块写的删除数据脚本，从mysql_del.txt里提取字段。这里用的是网页的url。
'''

import MySQLdb
#阿里云服务器
conn = MySQLdb.connect(
    host="120.76.242.206", port=3306, user="cnki5631", passwd="cnkipassword5631", db="caiji_shs", charset="utf8"
)
#Ubuntu服务器
#conn = MySQLdb.connect(host="192.168.58.129", port=3306, user="root", passwd="mysql", db="test2", charset="utf8")
print("start running ...")
with open("mysql_del.txt", "r") as files:
    while True:
        url = files.readline().split("\n")[0]
        if url == "":
            break
        else:
            cs = conn.cursor()
            sql = 'delete from crawler_content where f_page_url="%s"' % url
            exe = cs.execute(sql)
            conn.commit()
            cs.close()
conn.close()
print("run complete!")
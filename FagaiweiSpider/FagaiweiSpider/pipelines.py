# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import os
from scrapy.pipelines.files import FilesPipeline
from scrapy.utils.project import get_project_settings
import MySQLdb.cursors

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from twisted.enterprise import adbapi
import copy
import urllib2
from FagaiweiSpider import settings
import redis
from scrapy.exceptions import DropItem


class FagaiweispiderPipeline(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool
        self.f_job_name = ""

    @classmethod
    def from_crawler(cls, crawler):
        WRITE_DATE = crawler.settings.get("WRITE_DATE")
        dbpool = adbapi.ConnectionPool("MySQLdb", **WRITE_DATE)
        return cls(dbpool)

    def process_item(self, item, spider):
       if item:
            if item["myproject"] == "环保部":
                self.f_job_name = "zhb"
            elif item["myproject"] == "水利部":
                self.f_job_name = "mwr"
            elif item["myproject"] == "发改委":
                self.f_job_name = "sdpc"
            elif item["myproject"] == "国土资源部":
                self.f_job_name = "mlr"
            elif item["myproject"] == "农业部":
                self.f_job_name = "moa"
            asynitem = copy.deepcopy(item)
            query = self.dbpool.runInteraction(self._do_upinsert,asynitem, spider)
            #query.addErrback(self._handler_error, item, spider)
            query.addBoth(lambda _: item)

            # if "num" in asynitem.keys():
            #     for i in range(asynitem["num"]):
            #         attachment = "attachment%s" %str(i)
            #         pdf_url = asynitem[attachment]
            #         url_name = "pdf_name%s" %str(i)
            #         pdf_name = asynitem[url_name]
            #         pdf_path = "%s/%s/%s" %(settings.FILES_STORE, item["myproject"], pdf_name)
            #
            #         #附件名字已经存在跳过
            #         if os.path.exists(pdf_name):
            #             continue
            #         else:
            #             #如果是邮箱地址或者网页跳过,否则下载附件
            #             if pdf_path.endswith("cn") or pdf_path.endswith("/") \
            #                     or pdf_path.endswith("html") or pdf_path.endswith("com") \
            #                     or pdf_path.endswith("gov") or pdf_path.endswith("htm") \
            #                     or pdf_path.endswith("shtml")or pdf_path.endswith("mal") \
            #                       or pdf_path.endswith("1") or pdf_path.endswith("0") \
            #                       or pdf_path.endswith("0"):
            #                 continue
            #             else:
            #                 with open(pdf_path, "wb") as file_writer:
            #                     conn = urllib2.urlopen(pdf_url)
            #                     # file_writer.write(conn.read())
            #                     done = 0
            #                     while not done:
            #                         date = conn.readline()
            #                         if date != "":
            #                             file_writer.write(date)
            #                         else:
            #                             done = 1
            #                 file_writer.close()
            #     return item
            #
            #
            if "images_num" in asynitem.keys():
                for i in range(asynitem["images_num"]):
                    images = "images%s" %str(i)
                    images_source_url = asynitem[images]
                    images_name = "images_name%s" %str(i)
                    images_path_name = asynitem[images_name]
                    images_path = "%s\\%s\\%s" %(settings.FILES_STORE, self.f_job_name, images_path_name)
                    #检测图片是否存在
                    if os.path.exists(images_path_name):
                        continue
                    else:
                        with open(images_path, "wb") as file_writer:
                            conn = urllib2.urlopen(images_source_url)
                            file_writer.write(conn.read())
                        file_writer.close()
                return item
            return query

    def _do_upinsert(self, conn, item, spider):
        if item:
            conn.executemany(
                    'insert into crawler_content(f_job_name, f_article_title, f_article_time, f_article_content, f_page_url, f_after_content, f_fetchtime, f_file) \
                  values(%s, %s, %s, %s, %s, %s, %s, %s)',
                    [(
                        item["myproject"],
                        item["title"],
                        item["uptime"],
                        item["content"],
                        item["source"],
                        item["content_text"],
                        item["crawl_time"],
                        item["f_file"]
                    )]
            )


class InsertRideis(object):

    def process_item(self, item, spider):
        r = redis.StrictRedis(host='localhost', port=6379, db=1)
        if r.exists("%s" % item["source"]):
            raise DropItem("Duplicate item found: %s" %item["source"])
        else:
            r.set("%s" % item["source"], 1)
            return item


class InsertPDFpath(object):
    def __init__(self):
        self.f_job_name = ""

    def process_item(self, item, spider):
        if item:
            if item["myproject"] == "环保部":
                self.f_job_name = "zhb"
            elif item["myproject"] == "水利部":
                self.f_job_name = "mwr"
            elif item["myproject"] == "发改委":
                self.f_job_name = "sdpc"
            elif item["myproject"] == "国土资源部":
                self.f_job_name = "mlr"
            elif item["myproject"] == "农业部":
                self.f_job_name = "moa"
            r = redis.StrictRedis(host='localhost', port=6379, db=2)
            if "num" in item.keys():
                for i in range(item["num"]):
                    attachment = "attachment%s" %str(i)
                    pdf_url = item[attachment]
                    url_name = "pdf_name%s" %str(i)
                    pdf_name = item[url_name]
                    pdf_path = "%s\\%s\\%s" %(settings.FILES_STORE, self.f_job_name, pdf_name)
                #如果
                    if pdf_path.endswith("cn") or pdf_path.endswith("/") \
                            or pdf_path.endswith("html") or pdf_path.endswith("com") \
                            or pdf_path.endswith("gov") or pdf_path.endswith("htm") \
                            or pdf_path.endswith("shtml")or pdf_path.endswith("mal"):
                        continue
                    else:
                        r.set("%s" %pdf_path, "%s" %pdf_url)
            return item


















# -*- coding: utf-8 -*-
import scrapy
import re
import time
from lxml import etree
from FagaiweiSpider.items import FagaiweispiderItem



class GongwenSpider(scrapy.Spider):
    name = "nong_gongwen"
    allowed_domains = ["www.moa.gov.cn"]

    start_list = [
        #'http://www.moa.gov.cn/govpublic/', #首页
    ]
    i = 1
    start_list.append("http://www.moa.gov.cn/govpublic/22/23/index_1148.htm")
    while i<21:

        url = "http://www.moa.gov.cn/govpublic/22/23/index_1148_%s.htm" %str(i)
        start_list.append(url)
        i+=1
    start_list.append("http://www.moa.gov.cn/govpublic/22/24/index_1148.htm")
    i = 1
    while i<110:
        url = "http://www.moa.gov.cn/govpublic/22/24/index_1148_%s.htm" %str(i)
        start_list.append(url)
        i+=1
    start_list.append("http://www.moa.gov.cn/govpublic/22/25/index_1148.htm")
    i = 1
    while i<417:

        url = "http://www.moa.gov.cn/govpublic/22/25/index_1148_%s.htm" %str(i)
        start_list.append(url)
        i+=1
    start_list.append("http://www.moa.gov.cn/govpublic/22/26/index_1148.htm")
    i = 1
    while i<136:

        url = "http://www.moa.gov.cn/govpublic/22/26/index_1148_%s.htm" %str(i)
        start_list.append(url)
        i+=1
    start_list.append("http://www.moa.gov.cn/govpublic/22/27/index_1148.htm")
    i = 1
    while i<21:

        url = "http://www.moa.gov.cn/govpublic/22/27/index_1148_%s.htm" %str(i)
        start_list.append(url)
        i+=1
    start_list.append("http://www.moa.gov.cn/govpublic/22/28/index_1148.htm")
    i = 1
    while i<235:

        url = "http://www.moa.gov.cn/govpublic/22/28/index_1148_%s.htm" %str(i)
        start_list.append(url)
        i+=1
    start_list.append("http://www.moa.gov.cn/govpublic/22/29/index_1148.htm")
    i = 1
    while i<49:

        url = "http://www.moa.gov.cn/govpublic/22/29/index_1148_%s.htm" %str(i)
        start_list.append(url)
        i+=1
    start_list.append("http://www.moa.gov.cn/govpublic/22/30/index_1148.htm")
    i = 1
    while i<199:

        url = "http://www.moa.gov.cn/govpublic/22/30/index_1148_%s.htm" % str(i)
        start_list.append(url)
        i += 1
    start_list.append("http://www.moa.gov.cn/govpublic/22/31/index_1148.htm")
    i = 1
    while i<20:

        url = "http://www.moa.gov.cn/govpublic/22/31/index_1148_%s.htm" % str(i)
        start_list.append(url)
        i += 1
    start_list.append("http://www.moa.gov.cn/govpublic/22/32/index_1148.htm")
    i = 1
    while i<55:

        url = "http://www.moa.gov.cn/govpublic/22/32/index_1148_%s.htm" % str(i)
        start_list.append(url)
        i += 1
    start_list.append("http://www.moa.gov.cn/govpublic/22/33/index_1148.htm")
    i = 1
    while i<23:

        url = "http://www.moa.gov.cn/govpublic/22/33/index_1148_%s.htm" % str(i)
        start_list.append(url)
        i += 1
    start_list.append("http://www.moa.gov.cn/govpublic/22/34/index_1148.htm")
    i = 1
    while i<14:

        url = "http://www.moa.gov.cn/govpublic/22/34/index_1148_%s.htm" % str(i)
        start_list.append(url)
        i += 1
    start_list.append("http://www.moa.gov.cn/govpublic/22/35/index_1148.htm")
    i = 1
    while i<37:

        url = "http://www.moa.gov.cn/govpublic/22/35/index_1148_%s.htm" % str(i)
        start_list.append(url)
        i += 1
    start_list.append("http://www.moa.gov.cn/govpublic/22/58/index_1148.htm")
    i = 1
    while i<83:

        url = "http://www.moa.gov.cn/govpublic/22/58/index_1148_%s.htm" % str(i)
        start_list.append(url)
        i += 1
    start_list.append("http://www.moa.gov.cn/govpublic/22/36/index_1148.htm")
    i = 1
    while i<385:

        url = "http://www.moa.gov.cn/govpublic/22/36/index_1148_%s.htm" % str(i)
        start_list.append(url)
        i += 1

    start_urls = start_list

    def parse(self, response):

        url_list = response.xpath("//li/a/@href").extract()
        title_list = response.xpath("//li/a").extract()
        uptime_list = response.xpath("//li/div[@class='rowInRecord clr2']/span[last()]/text()").extract()

        if url_list != []:
            for i in range(len(url_list)):
                item = FagaiweispiderItem()
                item['title'] = etree.HTML(title_list[i]).xpath("//a/text()")[0]
                item['uptime'] = uptime_list[i]
                sun_url = u"http://www.moa.gov.cn/govpublic/"+url_list[i][6:]
                item["source"] = sun_url
                item["f_file"] = ""

                yield scrapy.Request(url=item['source'], callback=self.next_parse, meta={"item":item})

    def next_parse(self, response):
        item = response.meta["item"]

        content = response.xpath("//div[@class='content']").extract()[0]
        attachment_list = response.xpath("//div[@class='appendix']/a/@href|//div[@id='appendix']/a/@href").extract()
        content_attachment = response.xpath("//div[@id='appendix']").extract()

        item["myproject"] = "农业部"
        item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


        content_text = re.sub(r'<script[^>]*?>.*?</script>',"",content)
        content_text = re.sub(r'<style[^>]*?>[\s\S]*?</style>',"",content_text).strip()
        content_text = re.sub(r'<[^>]*?>',"",content_text).strip()
        item["content_text"] = re.sub(r"&", "", content_text)
        # 处理有多个附件的情况
        if attachment_list != []:
            # 附件计数器
            item["num"] = len(attachment_list)
            new_pdf_url_content = content + content_attachment[0]
            # 处理附件真是地址与更换附件url
            for i in range(len(attachment_list)):
                # 拼接pdf数据来源地址，交给pipelines
                pdf_url = re.match(r'.+/', response.url).group() + attachment_list[i][2:]
                pdf_name = "pdf_name%s" % str(i)
                # 保存附件文件名
                file_path = attachment_list[i].split("/")[-1]
                item[pdf_name] = file_path
                attachment_name = "attachment%s" % str(i)
                item[attachment_name] = pdf_url

                # 如果附件是正文中的邮箱地址或者网页链接跳过循环
                url_num = len(attachment_list)
                if attachment_list[i].endswith("cn") or attachment_list[i].endswith("/") \
                        or attachment_list[i].endswith("html") or attachment_list[i].endswith("com") \
                        or attachment_list[i].endswith("gov"):
                    url_num -= 1
                    if url_num < 0:
                        item["content"] = new_pdf_url_content
                    continue

                else:
                    # 更换附件地址为本地的相对地址
                    load_pdf_url = "index/images/" + "moa" + "/" + file_path

                    new_pdf_url_content = re.sub(attachment_list[i], load_pdf_url, new_pdf_url_content)
                    item["content"] = new_pdf_url_content

        else:
            item["content"] = content

        yield item

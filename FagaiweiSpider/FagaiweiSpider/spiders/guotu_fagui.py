# -*- coding: utf-8 -*-
import scrapy
import re
import time
from lxml import etree

from FagaiweiSpider.items import FagaiweispiderItem


class GuotufaguiSpider(scrapy.Spider):
    name = "guotu_fagui"
    allowed_domains = ["mlr.gov.cn"]

    start_list = [
        "http://www.mlr.gov.cn/zwgk/flfg/tdglflfg/",
        "http://www.mlr.gov.cn/zwgk/flfg/tdglflfg/index_1.htm",
        "http://www.mlr.gov.cn/zwgk/flfg/tdglflfg/index_2.htm",
        "http://www.mlr.gov.cn/zwgk/flfg/tdglflfg/index_3.htm",
        "http://www.mlr.gov.cn/zwgk/flfg/tdglflfg/index_4.htm",
        "http://www.mlr.gov.cn/zwgk/flfg/kczyflfg/",
        "http://www.mlr.gov.cn/zwgk/flfg/kczyflfg/index_5.htm",
        "http://www.mlr.gov.cn/zwgk/flfg/kczyflfg/index_4.htm",
        "http://www.mlr.gov.cn/zwgk/flfg/kczyflfg/index_3.htm",
        "http://www.mlr.gov.cn/zwgk/flfg/kczyflfg/index_2.htm",
        "http://www.mlr.gov.cn/zwgk/flfg/kczyflfg/index_1.htm",
        "http://www.mlr.gov.cn/zwgk/flfg/hyglflfg/",
        "http://www.mlr.gov.cn/zwgk/flfg/hyglflfg/index_2.htm",
        "http://www.mlr.gov.cn/zwgk/flfg/hyglflfg/index_1.htm",
        "http://www.mlr.gov.cn/zwgk/flfg/dzhjgl/",
        "http://www.mlr.gov.cn/zwgk/flfg/chglflfg/",
        "http://www.mlr.gov.cn/zwgk/flfg/chglflfg/index_1.htm",
        "http://www.mlr.gov.cn/zwgk/flfg/zhgl/",
        "http://www.mlr.gov.cn/zwgk/flfg/dfflfg/",
        "http://www.mlr.gov.cn/zwgk/flfg/dfflfg/index_16.htm",
        "http://www.mlr.gov.cn/zwgk/flfg/xgflfg/",
        "http://www.mlr.gov.cn/zwgk/flfg/xgflfg/index_4.htm",
        "http://www.mlr.gov.cn/zwgk/flfg/xgflfg/index_3.htm",
        "http://www.mlr.gov.cn/zwgk/flfg/xgflfg/index_2.htm",
        "http://www.mlr.gov.cn/zwgk/flfg/xgflfg/index_1.htm",
        "http://www.mlr.gov.cn/zwgk/flfg/sfjs/",
        "http://www.mlr.gov.cn/zwgk/flfg/gtzybl/",
        "http://www.mlr.gov.cn/zwgk/flfg/gtzybl/index_1.htm",
    ]
    i = 1
    while i < 16:
        url = "http://www.mlr.gov.cn/zwgk/flfg/dfflfg/index_%s.htm" %str(i)
        start_list.append(url)
        i+=1

    start_urls = start_list

    def parse(self, response):
        title_list = response.xpath("//table[@id='con']/tr/td/a/text()|//table[@id='con']/tr/td/a/font/text()").extract()
        uptime_list = response.xpath("//table[@id='con']/tr/td[3]/text()").extract()
        sun_url_list = response.xpath("//table[@id='con']/tr/td/a/@href").extract()

        for i in range(len(sun_url_list)):
            item = FagaiweispiderItem()
            item["title"] = title_list[i]
            attachment = sun_url_list[i]
            if uptime_list != []:
                item["uptime"] = uptime_list[i]
            else:
                item["uptime"] = ""

            if attachment.startswith("./"):
                if attachment.endswith("htm"):
                    sun_url = re.match(r".+/", response.url).group() + attachment[2:]
                    item["source"] = sun_url
                    item["f_file"] = ""
                    yield scrapy.Request(url=item["source"], callback=self.next_parse, meta={"item":item})

                else:
                    item["num"] = 1
                    item["attachment0"] = sun_url
                    item['source'] = sun_url
                    item["myproject"] = "国土资源部"
                    item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    file_path = attachment.split("/")[-1]
                    item["pdf_name0"] = file_path
                    item["f_file"] = "index/images/" + "mlr" + "/" + file_path
                    item["content"] = ""
                    item["content_text"] = ""

                    yield item
            elif attachment.startswith("../../../"):
                sun_url = "http://www.mlr.gov.cn/" + attachment[9:]
                item["source"] = sun_url
                item["f_file"] = ""
                yield scrapy.Request(url=item["source"], callback=self.next_parse, meta={"item": item})

            elif attachment.startswith("../../"):
                sun_url = "http://www.mlr.gov.cn/" + attachment[6:]
                item["source"] = sun_url
                item["f_file"] = ""
                yield scrapy.Request(url=item["source"], callback=self.next_parse, meta={"item": item})

            elif attachment.startswith("http"):
                sun_url = attachment
                item["source"] = sun_url
                item["f_file"] = ""
                yield scrapy.Request(url=item["source"], callback=self.next_parse, meta={"item": item})
            #处理../的情况
            else:
                if attachment.endswith("htm"):
                    sun_url = re.match(r".+/", response.url).group()
                    new_url = sun_url.rstrip("/")
                    sun_url = re.match(r".+/", new_url).group() + attachment[3:]
                    item["source"] = sun_url
                    item["f_file"] = ""
                    yield scrapy.Request(url=item["source"], callback=self.next_parse, meta={"item": item})
                else:
                    item["num"] = 0
                    item["attachment0"] = sun_url
                    item['source'] = sun_url
                    item["myproject"] = "国土资源部"
                    item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    file_path = attachment.split("/")[-1]
                    item["pdf_name0"] = file_path
                    item["f_file"] = "index/images/" + "mlr" + "/" + file_path
                    item["content"] = ""
                    item["content_text"] = ""

                    yield item

    def next_parse(self, response):
        item = response.meta["item"]

        content = response.xpath("//table[@id='doccon']|//table[@height='45']|//div[@class='container']").extract()[0]
        url_list = response.xpath("//td[@class='f14']/ol/descendant::*/@href|//div[@align='left']/a/@href").extract()

        content_text = re.sub(r"<script[^>]*?>.*?</script>", "", content)
        content_text = re.sub(r'<style[^>]*?>[\s\S]*?</style>',"",content_text).strip()
        content_text = re.sub(r"<[^>]*>","",content_text).strip()
        item["content_text"] = re.sub(r"&", "", content_text)
        item["myproject"] = "国土资源部"
        item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        if url_list != []:
            new_pdf_url_content = content

            for i in range(len(url_list)):
                attachment_url = url_list[i]
                if attachment_url.startswith("./"):
                    item["num"] = len(url_list)
                    pdf_source_url = re.match(r".+/", response.url).group() + attachment_url[2:]
                    pdf_name = "pdf_name%s" % str(i)
                    # 保存附件文件名
                    file_path = attachment_url.split("/")[-1]
                    item[pdf_name] = file_path
                    attachment_name = "attachment%s" % str(i)
                    item[attachment_name] = pdf_source_url

                    # 更换附件地址为本地的相对地址
                    load_pdf_url = "index/images/" + "mlr" + "/" + file_path

                    new_pdf_url_content = re.sub(attachment_url, load_pdf_url, new_pdf_url_content)
                    item["content"] = new_pdf_url_content

                    #测试
                    yield item
                else:
                    item["content"] = content

        else:
            item["content"] = content

        #yield item

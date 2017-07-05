# -*- coding: utf-8 -*-
import scrapy
import re
import time
from lxml import etree

from FagaiweiSpider.items import FagaiweispiderItem


class GuotuqitaSpider(scrapy.Spider):
    name = "guotu_qita"
    allowed_domains = ["mlr.gov.cn"]

    start_list = [
        "http://www.mlr.gov.cn/zwgk/gkgd/",
        "http://www.mlr.gov.cn/zwgk/gkbg/2016/",
        "http://www.mlr.gov.cn/zwgk/gkbg/2016/index_1.htm",
        "http://www.mlr.gov.cn/zwgk/gkbg/2015/",
        "http://www.mlr.gov.cn/zwgk/gkbg/2015/index_1.htm",
        "http://www.mlr.gov.cn/zwgk/gkbg/2014/",
        "http://www.mlr.gov.cn/zwgk/gkbg/2014/index_1.htm",
        "http://www.mlr.gov.cn/zwgk/gkbg/2013/",
        "http://www.mlr.gov.cn/zwgk/gkbg/2012/",
        "http://www.mlr.gov.cn/zwgk/gkbg/2011/",
        "http://www.mlr.gov.cn/zwgk/gkbg/2010/",
        "http://www.mlr.gov.cn/zwgk/gkbg/2010/index_3.htm",
        "http://www.mlr.gov.cn/zwgk/gkbg/2010/index_2.htm",
        "http://www.mlr.gov.cn/zwgk/gkbg/2010/index_1.htm",
        "http://www.mlr.gov.cn/zwgk/gkbg/2009/",
        "http://www.mlr.gov.cn/zwgk/gkbg/2009/index_1.htm",
        "http://www.mlr.gov.cn/zwgk/gkbg/2008/",
        "http://www.mlr.gov.cn/zwgk/gkbg/2008/index_1.htm",
        "http://www.mlr.gov.cn/tdzt/zhgl/jzfqfg/qd/",
        "http://data.mlr.gov.cn/gtzygb/",
        "http://www.mlr.gov.cn/sjpd/tjsj/",
        "http://www.mlr.gov.cn/zwgk/zytz/",
    ]
    i = 1
    while i<34:
        url = "http://www.mlr.gov.cn/zwgk/zytz/index_%s.htm" %str(i)
        start_list.append(url)
        i+=1
    #start_list测试的时候暂时注释。
    #start_urls = start_list
    start_urls = ("http://www.mlr.gov.cn/zwgk/zytz/index_14.htm",)

    def parse(self, response):
        title_list = response.xpath("//table[@id='con']/tr/td/a").extract()
        #title_list = response.xpath("//table[@id='con']/tr/td/a/text()").extract()
        uptime_list = response.xpath("//table[@id='con']/tr/td[3]/text()").extract()
        url_list = response.xpath("//table[@id='con']/tr/td/a/@href").extract()

        for i in range(len(url_list)):
            item = FagaiweispiderItem()
            item["title"] = etree.HTML(title_list[i]).xpath("//a/text()")[0]
            item["uptime"] = uptime_list[i]
            attachment = url_list[i]

            if attachment.startswith("./"):
                sun_url = re.match(r".+/", response.url).group() + attachment[2:]
                item["source"] = sun_url

                if sun_url.endswith("htm"):
                    item["f_file"] = ""
                    yield scrapy.Request(url=item["source"], callback=self.next_parse, meta={"item":item})
                else:
                    item["num"] = 0
                    item["attachment0"] = sun_url
                    #item['source'] = sun_url
                    item["myproject"] = "国土资源部"
                    item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    file_path = re.search(r"/[A-Z].*", attachment).group()
                    item["pdf_name0"] = file_path
                    item["f_file"] = "index/images/" + "mlr" + "/" + file_path
                    item["content"] = ""
                    item["content_text"] = ""
                    yield item
            elif attachment.startswith("../"):
                sun_url = "http://www.mlr.gov.cn/zwgk/" + attachment[3:]
                item["source"] = sun_url

                if sun_url.endswith("htm"):
                    item["f_file"] = ""
                    yield scrapy.Request(url=item["source"], callback=self.next_parse, meta={"item": item})
                else:
                    item["num"] = 0
                    item["attachment0"] = sun_url
                    # item['source'] = sun_url
                    item["myproject"] = "国土资源部"
                    item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    file_path = re.search(r"/[A-Z].*", attachment).group()
                    item["pdf_name0"] = file_path
                    item["f_file"] = "index/images/" + "mlr" + "/" + file_path
                    item["content"] = ""
                    item["content_text"] = ""
                    yield item

            #结对地址的情况，可能会有重复页面
            else:
                if attachment.endswith("htm"):
                    sun_url = attachment
                    item["source"] = sun_url
                    item["f_file"] = ""
                    yield scrapy.Request(url=item['source'], callback=self.http_parse, meta={"item":item})
                else:
                    item["num"] = 1
                    item["attachment0"] = attachment
                    item["myproject"] = "国土资源部"
                    file_path = attachment.split("/")[-1]
                    item["f_file"] = "index/images/" + "mlr" + "/" + file_path
                    item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    item["pdf_name0"] = file_path
                    item["content"] = ""
                    item["content_text"] = ""
                    yield item


    def next_parse(self, response):
        item = response.meta["item"]
        content = response.xpath("//table[@id='doccon']|//div[@class='TRS_Editor']").extract()[0]
        ol_url = response.xpath("//ol/text()").extract()
        images_url = response.xpath("//p/img/@src|//div[@class='Custom_UnionStyle']/img/@src").extract()

        content_text = re.sub(r"<script[^>]*?>.*?</script>","",content)
        content_text = re.sub(r'<style[^>]*?>[\s\S]*?</style>',"",content_text).strip()
        content_text = re.sub(r"<[^>]*>","",content_text).strip()
        item["content_text"] = re.sub(r"&", "", content_text)
        item["myproject"] = "国土资源部"
        item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        if ol_url != []:
            html = ol_url[0]
            url_list = list(set(re.findall('<a\shref="([^"]*)"', html)))
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

        else:
            item["content"] = content

        if images_url != []:
            item["images_num"] = len(images_url)
            #如果考虑到同时有附件与图片的情况会更好。
            if ol_url != []:
                new_images_url_content = item["content"]
            else:
                new_images_url_content = content
            for i in range(len(images_url)):
                images_name = "images_name" + str(i)
                images_path = images_url[i].split("/")[-1]
                item[images_name] = images_path
                images_source_url = re.match(r".+/", response.url).group() + images_path
                images_source_url_name = "images" + str(i)
                item[images_source_url_name] = images_source_url

                content_text = re.sub(r"<script[^>]*?>.*?</script>", "", content)
                content_text = re.sub(r'<style[^>]*?>[\s\S]*?</style>',"",content_text).strip()
                item["content_text"] = re.sub(r"<[^>]*>", "", content_text)

                # 更换附件地址为本地的相对地址
                local_images_url = "index/images/" + "mlr" + "/" + images_path
                new_images_url_content = re.sub(images_url[i], local_images_url, new_images_url_content)
                item["content"] = new_images_url_content

        yield item


    def http_parse(self, response):
        item = response.meta['item']
        if "uptime" not in item.keys():
            uptime = response.xpath("//tr[3]/td[2]/text()").extract()[0]
            item["uptime"] = uptime
        content_header = response.xpath("//div[@class='table']").extract()
        content_body = response.xpath("//div[@class='article']").extract()
        url_list = response.xpath("//ol/a/@href").extract()
        if content_header == []:
            yield scrapy.Request(url=response.url, callback=self.next_parse, meta={"item":item})

        else:
            content = content_body[0]
            content = re.sub(r'<h3>[\s\S]*?</h3>', '', content)
            item["myproject"] = "国土资源部"
            content_text = re.sub(r"<script[^>]*?>.*?</script>", "", content)
            content_text = re.sub(r'<style[^>]*?>[\s\S]*?</style>',"",content_text).strip()
            item["content_text"] = re.sub(r"<[^>]*>", "", content_text)

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

                    # 经过测试附件是绝对地址的情况下，附件地址不存在，无法下载。
                    else:
                        item["content"] = content
                        #     pdf_source_url = attachment_url
                        #     pdf_name = "pdf_name%s" % str(i)
                        #     # 保存附件文件名
                        #     item[pdf_name] = attachment_url[2:]
                        #     attachment_name = "attachment%s" % str(i)
                        #     item[attachment_name] = pdf_source_url
                        #
                        #     # 更换附件地址为本地的相对地址
                        #     load_pdf_url = "./images/" + "mlr" + attachment_url[2:]
                        #
                        #     new_pdf_url_content = re.sub(attachment_url, load_pdf_url, new_pdf_url_content)
                        #     item["content"] = new_pdf_url_content

            else:
                item["content"] = content

            yield item


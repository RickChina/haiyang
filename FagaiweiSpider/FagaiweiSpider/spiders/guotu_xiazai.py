# -*- coding: utf-8 -*-
import scrapy
import re
import time
import urlparse
from lxml import etree

from FagaiweiSpider.items import FagaiweispiderItem


class GuotuxiazaiSpider(scrapy.Spider):
    name = "guotu_xiazai"
    allowed_domains = ["mlr.gov.cn"]

    start_urls = ["http://www.mlr.gov.cn/bsfw/xzfw/zll/"]

    def parse(self, response):
        title_list = response.xpath("//table[@id='con']/tr/td/a").extract()
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
                    yield scrapy.Request(url=item["source"], callback=self.next_parse, meta={"item": item})
                else:
                    item["num"] = 1
                    item["source"] = sun_url
                    item["attachment0"] = sun_url
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

            elif attachment.startswith("http"):
                sun_url = attachment
                item["num"] = 0
                item["attachment0"] = sun_url
                item['source'] = sun_url
                item["myproject"] = "国土资源部"
                item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                item["pdf_name0"] = attachment.split("/")[-1]
                item["f_file"] = "index/images/" + "mlr" + "/" + attachment.split("/")[-1]
                item["content"] = ""
                item["content_text"] = ""
                yield item

            elif attachment.startswith("/"):
                sun_url = "http://www.mlr.gov.cn/" + attachment
                item["num"] = 0
                item["attachment0"] = sun_url
                item['source'] = sun_url
                item["myproject"] = "国土资源部"
                item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                item["pdf_name0"] = attachment.split("/")[-1]
                item["f_file"] = "index/images/" + "mlr" + "/" + attachment.split("/")[-1]
                item["content"] = ""
                item["content_text"] = ""
                yield item

            else:
                sun_url = "http://www.mlr.gov.cn/bsfw/xzfw/" + attachment[3:]
                item["source"] = sun_url
                yield scrapy.Request(url=item["source"], callback=self.next_parse, meta={"item": item})


    def next_parse(self, response):
        item = response.meta["item"]
        content = response.xpath("//table[@id='doccon']|//div[@class='TRS_Editor']").extract()[0]
        url_list = response.xpath("//td[@class='f14']/ol/descendant::*/@href|//div[@align='left']/a/@href").extract()
        images_url = response.xpath("//p[@align='center']/img/@src|//div[@class='Custom_UnionStyle']/img/@src").extract()


        content_text = re.sub(r"<script[^>]*?>.*?</script>","",content)
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

                else:
                    item["content"] = content

        else:
            item["content"] = content

        if images_url != []:
            item["images_num"] = len(images_url)
            #如果考虑到同时有附件与图片的情况会更好。
            if url_list != []:
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

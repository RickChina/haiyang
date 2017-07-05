# -*- coding: utf-8 -*-
import scrapy
import re
import time
from lxml import etree

from FagaiweiSpider.items import FagaiweispiderItem


class GuotulanmuSpider(scrapy.Spider):
    name = "guotu_lanmu"
    allowed_domains = ["mlr.gov.cn"]

    start_list = [
        "http://g.mlr.gov.cn/index_3501.html",
    ]

    start_urls = start_list
    url_index = 1

    def parse(self, response):
        title_list = response.xpath("//td/a").extract()
        url_list = response.xpath("//td/a/@href").extract() 

        for i in range(len(url_list)):
            item = FagaiweispiderItem()
            item["title"] = etree.HTML(title_list[i]).xpath("//a/text()")[0]
            item["myproject"] = "国土资源部"
            item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            url = url_list[i]
            if url.startswith("./"):
                item["source"] = "http://g.mlr.gov.cn/" + url[2:]
                item["f_file"] = ""
                yield scrapy.Request(url=item["source"], callback=self.next_parse, meta={"item":item})
        
        if self.url_index < 187:
            url = "http://g.mlr.gov.cn/index_3501_%s.html" %str(self.url_index)
            self.url_index += 1
            yield scrapy.Request(url=url, callback=self.parse)
            
    def next_parse(self, response):
        item = response.meta['item']

        uptime = response.xpath("//tr/td[2]/text()").extract()[4]
        content_header = response.xpath("//div[@id='nocountry']|//div[@class='box']").extract()[0]
        content_body = response.xpath("//div[@id='content']").extract()[0]
        content_body = re.sub(r'<h3>[\s\S]*?</h3>','', content_body)
        url_list = response.xpath("//span[@id='fj']/a/@href").extract()
        images_url = response.xpath("//p/img/@src").extract()
        content = content_body

        item["uptime"] = ""
        content_text = re.sub(r"<script[^>]*?>.*?</script>","",content)
        content_text = re.sub(r'<style[^>]*?>[\s\S]*?</style>',"",content_text).strip()
        content_text = re.sub(r"<[^>]*>","",content_text).strip()
        item["content_text"] = re.sub(r"&", "", content_text)

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

                    #ceui
                    yield item

                #经过测试附件是绝对地址的情况下，附件地址不存在，不考虑。
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

                #ceui
                yield item
        #yield item


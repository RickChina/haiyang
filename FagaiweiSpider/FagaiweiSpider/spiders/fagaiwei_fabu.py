# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
import time
import urlparse
from FagaiweiSpider.items import FagaiweispiderItem
from lxml import etree


class FagaiweiFabuSpider(CrawlSpider):
    name = 'fagaiwei_fabu'
    allowed_domains = ['ndrc.gov.cn']
    start_list = []
    f = open("fagaiwei_url.txt","r")
    while True:
        url = f.readline()
        if url != '':
            url = url.split("\n")[0]
            start_list.append(url)
        else:
            break

    start_urls = start_list

    def parse(self, response):
        title_list = response.xpath('//ul[@class="list_02 clearfix"]//a').extract()
        uptime_list = response.xpath('//ul[@class="list_02 clearfix"]//font/text()').extract()
        sun_url_list = response.xpath('//ul[@class="list_02 clearfix"]//a/@href').extract()
        #next_page = response.xpath('//li[@class="L"]/a[last()-1]/@href').extract()
        for i in range(len(title_list)):
            item = FagaiweispiderItem()
            item["title"] = etree.HTML(title_list[i]).xpath("//a/text()")[0]
            item["uptime"] = uptime_list[i]
            sun_url = urlparse.urljoin(response.url, sun_url_list[i])
            item["source"] = sun_url
            item["myproject"] = "发改委"

            if sun_url.endswith("rar") or sun_url.endswith("docx") or sun_url.endswith("doc")\
                    or sun_url.endswith("pdf") or sun_url.endswith("xls") or sun_url.endswith("zip")\
                    or sun_url.endswith("xlsx"):
                item["num"] = 0
                item["attachment0"] = sun_url
                item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                file_path = re.search(r"/([A-Za-z]\d.*)", sun_url).group(1)
                item["pdf_name0"] = file_path
                item["f_file"] = "index/images/" + "sdpc" + "/" + file_path
                item["content"] = ""
                item["content_text"] = ""
                yield item
            else:
                item["f_file"] = ""
                yield scrapy.Request(url=sun_url, callback=self.parse_page, meta={"item": item})

                #如果有下一页，继续跟进（js加载无法获取）
        # if next_page != []:
        #     next_page_url = urlparse.urljoin(response.url, next_page[0])
        #     yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_page(self, response):
        item = response.meta["item"]

        raw_content = response.xpath('//div[@class="TRS_Editor"]|//div[@class="txt1"]').extract()[0]
        raw_content = re.sub(r'<script[^>]*?>[\s\S]*?</scripy>', '', raw_content)
        content = re.sub(r'<style[^>]*?>[\s\S]*?</style>', '', raw_content)

        images_list = response.xpath('//p//img/@scr').extract()
        url_list = response.xpath('//a[@class="menu"]/@href|//a[@target="_blank"]/@href|//p/a/@href').extract()

        content_text = re.sub(r"<[^>]*>", "", content).strip()
        item["content_text"] = re.sub(r"&", "", content_text)
        item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        if url_list != []:
            new_pdf_url_content = content
            for i in range(len(url_list)):
                attachment_url = url_list[i]
                item["num"] = len(url_list)
                pdf_source_url = urlparse.urljoin(response.url, attachment_url)
                pdf_name = "pdf_name%s" % str(i)
                # 保存附件文件名
                file_path = attachment_url.split("/")[-1]
                item[pdf_name] = file_path
                attachment_name = "attachment%s" % str(i)
                item[attachment_name] = pdf_source_url
                # 更换附件地址为本地的相对地址
                load_pdf_url = "index/images/" + "sdpc" + "/" + file_path
                new_pdf_url_content = re.sub(attachment_url, load_pdf_url, new_pdf_url_content)
                item["content"] = new_pdf_url_content

            #这一行为了获取带附件的文章地址（测试）
            #yield item

        else:
            item["content"] = content
        if images_list != []:
            item["images_num"] = len(images_list)
            #如果考虑到同时有附件与图片的情况会更好。
            new_images_url_content = content
            for i in range(len(images_list)):
                images_name = "images_name" + str(i)
                images_path = images_list[i].split("/")[-1]
                item[images_name] = images_path
                images_source_url = urlparse.urljoin(response.url, images_list[i])
                images_source_url_name = "images" + str(i)
                item[images_source_url_name] = images_source_url
                # 更换附件地址为本地的相对地址
                local_images_url = "index/images/" + "sdpc" + "/" + images_path
                if url_list != []:
                    new_images_url_content = re.sub(images_list[i], local_images_url, item["content"])
                    item["content"] = new_images_url_content
                else:
                    new_images_url_content = re.sub(images_list[i], local_images_url, new_images_url_content)
                    item["content"] = new_images_url_content

            #为了获取带图片的文章url
            #yield item

        #测试需要先注释掉
        yield item

# -*- coding: utf-8 -*-
import scrapy
from FagaiweiSpider.items import FagaiweispiderItem
import re
import time
from lxml import etree


class ShuibaogaoSpider(scrapy.Spider):
    name = "shui_baogao"
    allowed_domains = ["mwr.gov.cn"]

    start_urls = (
        "http://zwgk.mwr.gov.cn/zfxxgkndbg/",
    )

    def parse(self, response):
        title_list = response.xpath("//td[1]/a").extract()
        uptime_list = response.xpath("//td[@class='huise']/text()").extract()
        url_list = response.xpath("//td[1]/a/@href").extract()

        for i in range(len(url_list)):
            # 实例化item
            item = FagaiweispiderItem()
            item["title"] = etree.HTML(title_list[i]).xpath("//a/text()")[0]
            item["uptime"] = uptime_list[i]
            # 拼接出子url
            sun_url = re.match(r'.+/', response.url).group() + url_list[i][2:]

            item["source"] = sun_url
            item["f_file"] = ""
            yield scrapy.Request(url=item['source'], callback=self.next_parse, meta={"item": item})


    def next_parse(self, response):
        item = response.meta["item"]
        #正文带图片，带标签response.xpath("//td[@align='center']").extract()
        item["myproject"] = "水利部"
        item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        content = response.xpath("//td[@class='heise']|//div[@class='TRS_Editor']").extract()[0]
        images_url = response.xpath("//td[@class='heise']/descendant::p/img/@src").extract()

        if images_url !=[]:
            item["images_num"] = len(images_url)
            new_images_url_content = content
            for i in range(len(images_url)):
                images_name = "images_name" + str(i)
                item[images_name] = images_url[i][2:]
                images_source_url = re.match(r".+/", response.url).group() + images_url[i][2:]
                images_source_url_name = "images" + str(i)
                item[images_source_url_name] = images_source_url

                content_text = re.sub(r"<script[^>]*?>.*?</script>","",content)
                content_text = re.sub(r'<style[^>]*?>[\s\S]*?</style>',"",content_text).strip()
                content_text = re.sub(r"<[^>]*>","",content_text).strip()
                item["content_text"] = re.sub(r"&", "", content_text)
                # 更换附件地址为本地的相对地址
                local_images_url = "index/images/" + "mwr" + "/" + images_url[i][2:]
                new_images_url_content = re.sub(images_url[i], local_images_url, new_images_url_content)
                item["content"] = new_images_url_content


        else:
            content_text = re.sub(r"<script[^>]*?>.*?</script>", "", content)
            content_text = re.sub(r'<style[^>]*?>[\s\S]*?</style>',"",content_text).strip()
            content_text = re.sub(r"<[^>]*>","",content_text).strip()
            item["content_text"] = re.sub(r"&", "", content_text)
            item["content"] = content

        yield item

# -*- coding: utf-8 -*-
import scrapy
import re
import time

from FagaiweiSpider.items import FagaiweispiderItem


class ZhengceSpider(scrapy.Spider):
    name = "nong_zhengce"
    allowed_domains = ["www.moa.gov.cn"]

    start_list = [
        'http://www.moa.gov.cn/zwllm/ghjh/',
        'http://www.moa.gov.cn/zwllm/zcfg/flfg/',  #法律行政规定 35
        'http://www.moa.gov.cn/zwllm/zcfg/nybgz/',  #农业部规章 57
        'http://www.moa.gov.cn/zwllm/zcfg/qnhnzc/',  #强农惠农 3
        'http://www.moa.gov.cn/zwllm/zcfg/qtbmgz/',  #其他部门 67
        'http://www.moa.gov.cn/zwllm/zcfg/dffg/',  #地方规章 66
        'http://www.moa.gov.cn/zwllm/zcfg/xgjd/',  #相关解读 22
    ]
    i = 1
    while i<19:
        url = "http://www.moa.gov.cn/zwllm/ghjh/index_%s.htm" %str(i)
        start_list.append(url)
        i+=1
    i = 1
    while i<35:
        url = "http://www.moa.gov.cn/zwllm/zcfg/flfg/index_%s.htm" %str(i)
        start_list.append(url)
        i+=1
    i = 1
    while i<57:
        url = "http://www.moa.gov.cn/zwllm/zcfg/nybgz/index_%s.htm" %str(i)
        start_list.append(url)
        i+=1
    i = 1
    while i<3:
        url = "http://www.moa.gov.cn/zwllm/zcfg/qnhnzc/index_%s.htm" %str(i)
        start_list.append(url)
        i+=1
    i = 1
    while i<67:
        url = "http://www.moa.gov.cn/zwllm/zcfg/qtbmgz/index_%s.htm" %str(i)
        start_list.append(url)
        i+=1
    i = 1
    while i<66:
        url = "http://www.moa.gov.cn/zwllm/zcfg/dffg/index_%s.htm" %str(i)
        start_list.append(url)
        i+=1
    i = 1
    while i<22:
        url = "http://www.moa.gov.cn/zwllm/zcfg/xgjd/index_%s.htm" %str(i)
        start_list.append(url)
        i+=1
    start_urls = start_list

    def parse(self, response):

        uptime_list = response.xpath("//div[@class='rlr']/ul/li/span[last()]/text()").extract()
        url_list = response.xpath("//div[@class='rlr']/ul/li/span/a/@href").extract()
        #拼接新的子url
        for i in range(len(uptime_list)):
            item = FagaiweispiderItem()
            item["uptime"] = uptime_list[i]
            url = url_list[i]
            if url.startswith("./"):
                sun_url = re.match(r'.+/', response.url).group() + url[2:]
                if sun_url.endswith("htm"):
                    item["f_file"] = ""
                    item["source"] = sun_url
                    yield scrapy.Request(url=sun_url, callback=self.text_parse, meta={"item": item})
                #自链接可能是pdf或者word文件
                else:
                    item["title"] = response.xpath("//div[@class='rlr']/ul/li/span/a/text()").extract()[i]
                    item["num"] = 1
                    item["attachment0"] = sun_url
                    item['source'] = sun_url
                    item["myproject"] = "发改委"
                    item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    file_path = url.split("/")[-1]
                    item["pdf_name0"] = file_path
                    item["f_file"] = "index/images/" + "moa" + "/" + file_path
                    item["content"] = ""
                    item["content_text"] = ""

                    yield item
            #自链接可能是文件公布的绝对地址,不做处理
            #else:
                # item["source"] = url
                #
                # yield scrapy.Request(url=url, callback=self.text_parse, meta={"item": item})



    def text_parse(self, response):
        item = response.meta["item"]

        content = response.xpath("//div[@id='TRS_AUTOADD']|//div[@class='zlcont']").extract()[0]
        title = response.xpath("//div[@class='zleft']/h1/text()").extract()[0]
        attachment_url = response.xpath("//a[@class='link02']/@href|//div[@id='appendix']/a/@href").extract()

        item["title"] = title
        item["myproject"] = "农业部"
        item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        content_text = re.sub(r'<script[^>]*?>.*?</script>',"",content)
        content_text = re.sub(r'<style[^>]*?>[\s\S]*?</style>',"",content_text).strip()
        content_text = re.sub(r'<div[^>]*?class="annv">[\s\S]*</div>',"",content_text)
        content_text = re.sub(r'<[^>]*?>',"",content_text).strip()
        item["content_text"] = re.sub(r"&", "", content_text)
        #拼接附件url，保存,处理有多个附件的情况
        if attachment_url != []:
            item["num"] = len(attachment_url)
            new_pdf_url_content = content
            # 拼接pdf数据来源地址，交给pipelines
            for i in range(len(attachment_url)):
                pdf_url = re.match(r'.+/', response.url).group() + attachment_url[i][2:]
                pdf_name = "pdf_name%s" % str(i)
                # 保存附件文件名
                file_path = attachment_url[i].split("/")[-1]
                item[pdf_name] = file_path
                attachment_name = "attachment%s" % str(i)
                item[attachment_name] = pdf_url

                # 如果附件是正文中的邮箱地址或者网页链接跳过循环
                url_num = len(attachment_url)
                if attachment_url[i].endswith("cn") or attachment_url[i].endswith("/") \
                        or attachment_url[i].endswith("html") or attachment_url[i].endswith("com") \
                        or attachment_url[i].endswith("gov"):
                    url_num -= 1
                    if url_num < 0:
                        new_pdf_url_content = re.sub(
                            r'<div[^>]*?class="annv".*>[\s\S]*</div>',"</div>",new_pdf_url_content
                        )
                        new_pdf_url_content = re.sub(
                            r'<div[^>]*?class="bot".*>[\s\S]*</div>', "</div>",new_pdf_url_content
                        )
                        item["content"] = new_pdf_url_content
                    continue

                else:
                    # 更换附件地址为本地的相对地址
                    load_pdf_url = "index/images/" + "moa" + "/" + file_path

                    new_pdf_url_content = re.sub(attachment_url[i], load_pdf_url, new_pdf_url_content)
                    new_pdf_url_content = re.sub(
                        r'<div[^>]*?class="annv".*>[\s\S]*</div>',"</div>",new_pdf_url_content
                    )
                    new_pdf_url_content = re.sub(
                        r'<div[^>]*?class="bot".*>[\s\S]*</div>', "</div>", new_pdf_url_content
                    )
                    item["content"] = new_pdf_url_content

        else:
            content = re.sub(r'<div[^>]*?class="annv".*>[\s\S]*</div>',"</div>",content)
            content = re.sub(r'<div[^>]*?class="bot".*>[\s\S]*</div>', "</div>", content)
            item["content"] = content

        yield item







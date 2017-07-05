# -*- coding: utf-8 -*-
import scrapy
from FagaiweiSpider.items import FagaiweispiderItem
import re
import time


class ShuilibuSpider(scrapy.Spider):
    name = "shuilibu"
    allowed_domains = ["mwr.gov.cn"]

    start_list = [
        "http://www.mwr.gov.cn/zwzc/zcfg/fl/",
        "http://www.mwr.gov.cn/zwzc/ghjh/",
        "http://www.mwr.gov.cn/zwzc/zcfg/xzfghfgxwj/",
        "http://www.mwr.gov.cn/zwzc/zcfg/bmfggfxwj/",
        "http://www.mwr.gov.cn/zwzc/zcfg/jd/",
        "http://www.mwr.gov.cn/zwzc/gwywj/",
        "http://www.mwr.gov.cn/zwzc/jbjc/sljb/",
        "http://www.mwr.gov.cn/zwzc/jbjc/slxwhjb/",
        "http://www.mwr.gov.cn/zwzc/jbjc/ntslhbjsjb/",
        "http://www.mwr.gov.cn/zwzc/jbjc/slfpjb/",

    ]
    i = 1
    while i<21:  #规划计划
        url = "http://www.mwr.gov.cn/zwzc/ghjh/index_%s.html" %str(i)
        start_list.append(url)
        i+=1
    i = 1
    while i<2:  #政策法规～行政法规文件
        url = "http://www.mwr.gov.cn/zwzc/zcfg/xzfghfgxwj/index_%s.html" %str(i)
        start_list.append(url)
        i+=1
    i = 1
    while i<10:  #政策法规～部门规章
        url = "http://www.mwr.gov.cn/zwzc/zcfg/bmfggfxwj/index_%s.html" %str(i)
        start_list.append(url)
        i+=1
    i = 1
    while i<2:  #政策法规～政策解读
        url = "http://www.mwr.gov.cn/zwzc/zcfg/jd/index_%s.html" %str(i)
        start_list.append(url)
        i+=1
    i = 1
    while i<7:  #国务院文件
        url = "http://www.mwr.gov.cn/zwzc/gwywj/index_%s.html" %str(i)
        start_list.append(url)
        i+=1
    i = 1
    while i<21:  #水利简报
        url = "http://www.mwr.gov.cn/zwzc/jbjc/sljb/index_%s.html" %str(i)
        start_list.append(url)
        i+=1
    #一下代码无法获取
    # start_list.append("http://www.mwr.gov.cn/zwzc/jbjc/aqscjb/")
    # while i<2:  #水利安全成产简报
    #
    #     url = "http://www.mwr.gov.cn/zwzc/jbjc/aqscjb/index_%s.html" %str(i)
    #     start_list.append(url)
    #     i+=1
    i = 1
    while i<5:  #水利信息话简报
        url = "http://www.mwr.gov.cn/zwzc/jbjc/slxwhjb/index_%s.html" %str(i)
        start_list.append(url)
        i+=1
    i = 1
    while i<11:  #农田水利基本建设简报
        url = "http://www.mwr.gov.cn/zwzc/jbjc/ntslhbjsjb/index_%s.html" %str(i)
        start_list.append(url)
        i+=1
    i = 1
    while i<5:  #水利扶贫简报
        url = "http://www.mwr.gov.cn/zwzc/jbjc/slfpjb/index_%s.html" %str(i)
        start_list.append(url)
        i+=1
    #水电工作
    start_list.append("http://www.mwr.gov.cn/zwzc/jbjc/ncsdgzxx/")
    #水利部公报
    start_list.append("http://www.mwr.gov.cn/zwzc/hygb/slbgb/")
    start_list.append("http://www.mwr.gov.cn/zwzc/hygb/slbgb/index_1.html")
    #发展统计公报
    start_list.append("http://www.mwr.gov.cn/zwzc/hygb/slfztjgb/")
    #水资源公报
    start_list.append("http://www.mwr.gov.cn/zwzc/hygb/szygb/")
    start_list.append("http://www.mwr.gov.cn/zwzc/hygb/szygb/index_1.html")
    #河流公报
    start_list.append("http://www.mwr.gov.cn/zwzc/hygb/zghlnsgb/")
    #水利科技公报
    start_list.append("http://www.mwr.gov.cn/zwzc/hygb/slkjcggb/")
    #水寒灾害公报
    start_list.append("http://www.mwr.gov.cn/zwzc/hygb/zgshzhgb/")
    #中国水土保持公报
    start_list.append("http://www.mwr.gov.cn/zwzc/hygb/zgstbcgb/")
    #水温行业统计年报
    start_list.append("http://www.mwr.gov.cn/zwzc/hygb/swqknb/")
    #水清年报
    start_list.append("http://www.mwr.gov.cn/zwzc/hygb/sqnb/")
    start_list.append("http://www.mwr.gov.cn/zwzc/hygb/dxsdtyb/")
    i = 1
    while i<4:  #地下水月报
        url = "http://www.mwr.gov.cn/zwzc/hygb/dxsdtyb/index_%s.html" %str(i)
        start_list.append(url)
        i+=1
    start_list.append("http://www.mwr.gov.cn/zwzc/hygb/zysljstztjyb/")
    i = 1
    while i<3:  #中央水利建设投资统计
        url = "http://www.mwr.gov.cn/zwzc/hygb/zysljstztjyb/index_%s.html" %str(i)
        start_list.append(url)
        i+=1
    #小型水库建设
    start_list.append("http://www.mwr.gov.cn/zwzc/hygb/qgxxbxjggcqkyb/")
    start_list.append("http://www.mwr.gov.cn/zwzc/hygb/qgxxbxjggcqkyb/index_1.html")
    #水利水电年报
    start_list.append("http://www.mwr.gov.cn/zwzc/hygb/ncsdnb/")

    start_urls = start_list

    def parse(self, response):

        title_list = response.xpath("""//ul[@class='tg_t3']/li/a/text()|//ul[@id='ul_slb3']/li/a/text()|\
        //ul[@id='c']/li/a/text()""").extract()
        uptime_list = response.xpath("""//ul[@class='tg_t3']/li/span/text()|\
        //ul[@id='ul_slb3']/li/span/text()|//ul[@id='c']/li/span/text()""").extract()
        url_list = response.xpath("""//ul[@class='tg_t3']/li/a/@href|//ul[@id='ul_slb3']/li/a/@href|\
        //ul[@id='c']/li/a/@href""").extract()

        for i in range(len(url_list)):
            item =FagaiweispiderItem()
            sun_url = re.match(r".+/", response.url).group() + url_list[i][2:]
            item["title"] = title_list[i]
            item["uptime"] = uptime_list[i]
            item['source'] = sun_url

            if sun_url.endswith("html"):
                item["f_file"] = ""
                yield scrapy.Request(url=item["source"], callback=self.next_parse, meta={"item":item})

            elif sun_url.endswith("1") or sun_url.endswith("0") or sun_url.endswith("9"):
                continue

            else:
                item["num"] = 1
                item["attachment0"] = sun_url
                item["myproject"] = "水利部"
                item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                file_path = url_list[i].split("/")[-1]
                item["pdf_name0"] = file_path
                item["f_file"] = "index/images/" + "mwr" + "/" + file_path
                item["content"] = ""
                item["content_text"] = ""

                yield item

    def next_parse(self, response):
        item = response.meta["item"]
        content = response.xpath("//div[@id='maincontent']|//div[@id='maintablecontent']").extract()[0]
        attachment_block = response.xpath("//div[@style='padding-left:50px']").extract()[0]
        attachment_url = re.findall(r'href="(.*?)"', attachment_block)
        if attachment_url !=[]:
            item["myproject"] = "水利部"
            item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

            content_text = re.sub(r"<script[^>]*?>.*?</script>", "", content)
            content_pdf = content_text + "\n" + attachment_block
            content_text = re.sub(r'<style[^>]*?>[\s\S]*?</style>',"",content_pdf).strip()
            content_text = re.sub(r"<[^>]*>","",content_text).strip()
            item["content_text"] = re.sub(r"&", "", content_text)
            item["num"] = len(attachment_url)
            new_pdf_url_content = content_pdf

            for i in range(len(attachment_url)):
                pdf_url = re.match(r'.+/', response.url).group() + attachment_url[i][2:]
                pdf_name = "pdf_name%s" % str(i)
                # 保存附件文件名
                file_path = attachment_url[i].split("/")[-1]
                item[pdf_name] = file_path
                attachment_name = "attachment%s" % str(i)
                item[attachment_name] = pdf_url

                # 更换附件地址为本地的相对地址
                load_pdf_url = "index/images/" + "mwr" + "/" + file_path
                #print("=======================================")
                new_pdf_url_content = re.sub(attachment_url[i], load_pdf_url, new_pdf_url_content)
                item["content"] = new_pdf_url_content

        else:
            #print("+++++++++++++++++++++++++++++++++++++++++++")
            item["content"] = content
            item["myproject"] = "水利部"
            item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

            content_text = re.sub(r"<script[^>]*?>.*?</script>", "", content)
            content_text = re.sub(r'<style[^>]*?>[\s\S]*?</style>',"",content_text).strip()
            item["content_text"] = re.sub(r"<[^>]*>", "", content_text)

        yield item





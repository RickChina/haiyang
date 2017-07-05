# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FagaiweispiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    myproject = scrapy.Field()  # 项目
    title = scrapy.Field()  # 标题
    uptime = scrapy.Field()  # 时间
    content = scrapy.Field()  # 内容
    wirter = scrapy.Field()  # 作者
    source = scrapy.Field()  # 正文来源
    for i in range(70):
        locals()["attachment" + str(i)] = scrapy.Field()  # 附件 动态命名
        locals()["pdf_name" + str(i)] = scrapy.Field()  # 附件原本名字

        locals()["images"+str(i)] = scrapy.Field()
        locals()["images_name" + str(i)] = scrapy.Field()


    num = scrapy.Field()  #附件数量
    images_num = scrapy.Field() #图片计数器
    content_text = scrapy.Field() #不带标签的正文
    crawl_time = scrapy.Field() #爬取时间
    f_file = scrapy.Field() #网址直接是附件的相对地址
    prepare = scrapy.Field()  # 预备
    prepare2 = scrapy.Field()  # 预备2


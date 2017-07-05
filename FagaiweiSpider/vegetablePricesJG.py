#coding=utf-8

from selenium import webdriver
import datetime
import time
import os
from lxml import etree
import codecs
#可以尝试用urllib2
def infoCsv(website, maket, date, vegetable, price):
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    file_name = "%s.csv" % now
    lines = website + "," + maket + "," + date + "," + vegetable + "," + price + "\n"
    with open(file_name, "a") as files:
        files.write(lines)

def htmlParse(page_source):
    # 市场：market  日期：date  蔬菜：vegetable  价格：price  website:全国农产品价格数据库
    response = etree.HTML(page_source)
    market_list = response.xpath('//tr/td/a/text()')
    date_list = response.xpath('//tr/td[4]/text()')
    vegetable_list = response.xpath('//tr/td[1]/text()')
    price_list = response.xpath('//tr/td[2]/text()')
    if market_list != []:
        for i in range(len(market_list)):
            market = market_list[i].strip()
            date = date_list[i].strip()
            vegetable = vegetable_list[i].strip()
            price = price_list[i].strip()
            website = u"全国农产品价格数据库"
            infoCsv(website, market, date, vegetable, price)

def accessHtml(vegetables):
    driver = webdriver.Chrome()
    #构造今天和昨天的日期
    now = datetime.datetime.now()
    one_day = datetime.timedelta(days=1)
    yesterday = now - one_day
    now = now.strftime("%Y-%m-%d")
    yesterday = yesterday.strftime("%Y-%m-%d")
    url = "http://nc.mofcom.gov.cn%s&startTime=%s&endTime=%s&par_p_index=&p_index=&keyword=" % (
        vegetables, yesterday, now
    )
    driver.get(url)
    time.sleep(1)
    js = "document.body.scrollTop=500"
    driver.execute_script(js)
    time.sleep(1)
    source = driver.page_source
    if source == "EOF":
        driver.close()
        driver.get(url)
        source = driver.page_source
    #把源码交给数据解析模块
    htmlParse(source)
    while True:
        try:
            driver.find_element_by_class_name("next").click()
            time.sleep(1)
            source = driver.page_source
            # 把源码交给数据解析模块
            htmlParse(source)
            js = "document.body.scrollTop=500"
            driver.execute_script(js)
            time.sleep(1)
        except Exception:
            break
    driver.quit()

def mofcom():
    #取出vegetable.txt文件中的关键参数，构造url
    with open("vegetables.txt", "r") as files:
        while True:
            vegetable_name = files.readline()
            if vegetable_name != "":
                vegetables = vegetable_name.split(":")[0].strip("\s")
                #把数据交给页面渲染模块，拿到网页源码
                accessHtml(vegetables)
            else:
                break

if __name__ == "__main__":
    mofcom()
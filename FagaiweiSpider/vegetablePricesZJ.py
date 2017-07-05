#coding=utf-8

from selenium import webdriver
import datetime
import time
import os
from lxml import etree

def infoCsv(website, maket, date, vegetable, price):
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    file_name = "%s.csv" % now
    lines = website + "," + maket + "," + date + "," + vegetable + "," + price + "\n"
    with open(file_name, "a") as files:
        files.write(lines)

def htmlParse(page_source):
    # 市场：market  日期：date  蔬菜：vegetable  价格：price  website:浙江省农业厅
    response = etree.HTML(page_source)
    market_list = response.xpath('//td[@align="right"]//tr/td[5]/a/text()')
    date_list = response.xpath('//td[@align="right"]/table/tbody/tr[2]//table/tbody/tr[4]//tr/td[6]/text()')
    vegetable_list = response.xpath('//td[@align="right"]//tr/td[1]/a/text()')
    price_list = response.xpath('//td[@align="right"]/table/tbody/tr[2]//table/tbody/tr[4]//tr/td[2]/text()')
    if market_list != []:
        for i in range(len(market_list)):
            market = market_list[i]
            date = date_list[i]
            vegetable = vegetable_list[i]
            price = price_list[i]
            website = u"浙江省农业厅"
            infoCsv(website, market, date, vegetable, price)

def zjagri():
    driver = webdriver.PhantomJS()
    driver.get(
        "http://www.zjagri.gov.cn/programs/database/marketPrice/price/list.jsp?dq1=330000&dqjb=1&kd=1024"
    )
    #构造昨天日期，输入开始日期框
    now = datetime.datetime.now()
    one_day = datetime.timedelta(days=1)
    yesterday = now - one_day
    yesterday = yesterday.strftime("%Y-%m-%d")
    driver.find_element_by_name("ksrq").clear()
    driver.find_element_by_name("ksrq").send_keys(yesterday)
    driver.find_element_by_xpath('//a[@onclick="sousuo()"]').click()
    time.sleep(1)
    js = "document.body.scrollTop=200"
    driver.execute_script(js)
    time.sleep(1)
    source = driver.page_source
    #获取页面源码，交给解析模块处理
    htmlParse(source)
    #尝试获取下一页，并点击，获取源码给解析模块，报错提示爬虫结束。
    while True:
        try:
            driver.find_element_by_link_text("下页").click()
            time.sleep(2)
            source = driver.page_source
            htmlParse(source)
        except Exception:
            #print("Run complete!")
            break

    time.sleep(2)
    driver.quit()

if __name__ == "__main__":
    print("start running ...")
    zjagri()
    print("run complete!")
#coding=utf-8

'''农科院项目3个价格网站的启动文件，这里有另外两个文件的启用接口。可以直接运行命令生产csv文件。'''

from selenium import webdriver
import datetime
import time
import os
from lxml import etree
from vegetablePricesZJ import zjagri
from vegetablePricesJG import mofcom


def infoCsv(website, matket, date, vegetable, price):
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    file_name = "%s.csv" % now
    lines = website + "," + matket + "," + date + "," + vegetable + "," + price + "\n"
    with open(file_name, "a") as files:
        files.write(lines)

def sourceXpath(page_sourse):
    #市场：market  日期：date  蔬菜：vegetable  价格：price  website：江苏省农产品
    response = etree.HTML(page_sourse)
    market_list = response.xpath('//td[@class="LongStyle"]/text()')
    date_list = response.xpath('//td[@class="SubmitStyle"][1]/text()')
    vegetable_list = response.xpath('//td[@class="SubmitStyle"][2]/text()')
    price_list = response.xpath('//td[@class="SubmitStyle"][3]/text()')
    if market_list != []:
        for i in range(len(market_list)):
            market = market_list[i]
            date = date_list[i]
            vegetable = vegetable_list[i]
            price = price_list[i]
            #调用存入csv模块，把数据分条存入表格
            website = u"江苏省农产品价格信息报送系统"
            infoCsv(website, market, date, vegetable, price)

def jsagri():
    #先检查文件夹，如果存在同日期文件，删掉。
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    file_name = "%s.csv" % now
    if os.path.exists(file_name):
        os.remove(file_name)
    #开始爬虫
    driver = webdriver.PhantomJS()
    driver.get("http://market.jsagri.gov.cn/desktopmodules/getpricestat.aspx")
    #构造表单，输入今天日期
    driver.find_element_by_id("txtStartDate").clear()
    now = datetime.datetime.now()
    #构造昨天的日期
    one_day = datetime.timedelta(days=1)
    yesterday = now - one_day
    yesterday = yesterday.strftime("%Y-%m-%d")
    driver.find_element_by_id("txtStartDate").send_keys(yesterday)
    driver.find_element_by_id("btSearchName").click()
    time.sleep(2)
    js = "document.body.scrollTop=200"
    driver.execute_script(js)
    time.sleep(2)
    #获取源码解析数据
    source = driver.page_source
    #调用元素解析模块，提取市场，日期，品名，价格等数据。
    sourceXpath(source)
    #解析下一页
    last_page = driver.find_element_by_xpath('//td[@colspan="8"]/a[last()]').text
    NUM = 1
    while True:
        page_index = driver.find_element_by_xpath('//td[@colspan="8"]/a[%s]' % str(NUM)).text
        driver.find_element_by_xpath('//td[@colspan="8"]/a[%s]' % str(NUM)).click()
        time.sleep(2)
        # 获取源码解析数据
        source = driver.page_source
        # 调用元素解析模块，提取市场，日期，品名，价格等数据。
        sourceXpath(source)
        if page_index == last_page:
            break
        else:
            NUM+=1
    time.sleep(1)
    driver.quit()


if __name__ == '__main__':
    print("url=http://market.jsagri.gov.cn  start running ...")
    jsagri()
    print("url=http://market.jsagri.gov.cn  run complete!")
    print("url=http://market.zjagri.gov.cn  start running ...")
    zjagri()
    print("url=http://market.zjagri.gov.cn  run complete!")
    print("url=http://market.zjagri.gov.cn  start running ...")
    mofcom()
    print("url=http://market.zjagri.gov.cn  run complete!")
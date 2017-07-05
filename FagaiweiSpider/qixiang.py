#encoding=utf-8
import sys
reload (sys)
sys.setdefaultencoding('utf-8')

import random
import time
import MySQLdb
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#引入mysql数据库，去重与数据传递
def intoMysql(link):
    try:
        conn = MySQLdb.connect(
            host="120.76.242.206", port=3306, db="caiji_shs", user="cnki5631",
            passwd="cnkipassword5631", charset="utf8"
        )
        #cur.execute("select url from weather")
        #result = cur.fetchall()
        cur = conn.cursor()
        word = 'insert into weather(url) values("%s")' % link
        cur.execute(word)
        conn.commit()
        cur.close()
        # 标题  re.findall(r"(S\d+\.\D+)\?",a)
        conn.close()
    except Exception, e:
        print e

#这段代码可能会报两个错误，一个是验证码错误，另一个是进行中的订单没有数据。时间有限暂时没有处理。
driver = webdriver.Chrome()
driver.get("http://data.cma.cn/")
driver.find_element_by_class_name("loginhead").click()
time.sleep(1)
driver.find_element_by_id("loginWeb").click()
driver.find_element_by_id("userName").send_keys(u"mywilling@126.com")
driver.find_element_by_id("passwordFoot").send_keys(u"my20160830")
num = raw_input("Please enter the verification code, press Enter：")
driver.find_element_by_id("verifyCode").send_keys(num)
driver.find_element_by_id("login").click()
time.sleep(2)
driver.find_element_by_class_name("validfeedback ").click()
driver.find_element_by_id("cart-part-cont33").click()
#获取最后一个订单进行比对，确定订单数量
last_good_num = driver.find_element_by_xpath(
    '//div[@class="item1218 list1218 clearfix"][last()]/div[1]'
).text
i = 1
good_num_list = []
while True:
    select = '//div[@class="item1218 list1218 clearfix"][%s]/div[1]' % str(i)
    good_num = driver.find_element_by_xpath(select).text
    good_num_list.append(good_num)
    if good_num == last_good_num:
        break
    else:
        i += 1

#获取下载链接
for j in range(len(good_num_list)):
    j += 1
    select = '//div[@class="item1218 list1218 clearfix"][%s]/div[1]/i' % str(j)
    driver.find_element_by_xpath(select).click()
    link_select = '//div[@class="table-list-1218"][%s]//a[@class="down1218"]' % str(j)
    link = driver.find_element_by_xpath(link_select).get_attribute("href")
    #调用数据库
    intoMysql(link)




driver.find_element_by_class_name("loginoutA").click()
time.sleep(1)
driver.quit()
print("Congratulations, the task is done!")








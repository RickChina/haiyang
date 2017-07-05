#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import datetime
import re

my_sender="python_d@163.com" #发件人邮箱账号
my_user='python_d@163.com' #收件人邮箱账号
def mail():
    ret=True
    try:
        file_name ="logs\\\\%shy.log" % datetime.datetime.now().strftime("%Y-%m-%d")
        content = ""
        title = ""
        with open(file_name, "r") as fb:
            content = fb.read()
            error_num = re.findall("ERROR:", content)
            title = "海洋项目，error num : %d" % len(error_num)

        msg=MIMEText(content,'plain','utf-8')
        msg['From']=formataddr(["海洋服务器",my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["engineer",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']=title  #邮件的主题

        server=smtplib.SMTP("smtp.163.com",25)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender,"du123456")    #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   #关闭连接
    except Exception:
        ret=False
    return ret

ret=mail()
if ret:
    print("ok")
else:
    print("filed")
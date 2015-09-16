#!/usr/bin/env python
#coding=utf-8
#author: Ezreal
#email: osatmnzn@vip.qq.com
#version : 1.2
#desc: FOR SEND MAIL.

import sys, smtplib, os
#from datetime import date
#from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from email.mime.base import MIMEBase
#import email.iterators
#import email.generator
#from email import Encoders



#############
#读取邮件列表
file_object = open('list.txt')
try:
    all_the_text = file_object.readlines( )
finally:
    file_object.close( )
mailto_list = all_the_text

#读取配置文件
file_object = open('set.txt')
try:
    all_the_text = file_object.readlines( )
finally:
    file_object.close( )
set_list = all_the_text

#读取内容
file_object = open('html.txt')
try:
    all_the_text = file_object.readlines( )
finally:
    file_object.close( )
content_list = ''.join(all_the_text).replace("\n","")

#########格式化配置文件#############
def get_mail_fomat(index):
    return_str = set_list[index]
    return_str = return_str.replace("\n","")
    return_str = return_str.split('=')[1]
    return return_str

##########发送邮件############
def send_mail(to_list,sub,content,host,user,passwd,postfix,name):
    '''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    '''
    me=name+"<"+user+"@"+postfix+">"
    username = user+"@"+postfix
    msg = MIMEText(content,'html','utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    #msg['To'] = ";".join(to_list)
    msg['To'] = to_list
    try:
        server = smtplib.SMTP(host)
        #server.set_debuglevel(1)                               #邮件日志开关
        server.login(username,passwd)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

if __name__ == '__main__':
#def run():
    send_succeed_num = 0
    send_fail_num = 0
    #####################
    #设置服务器，用户名、口令,邮箱的后缀以及标题和内容
    mail_host = get_mail_fomat(0)
    mail_user = get_mail_fomat(1)
    mail_pass = get_mail_fomat(2)
    mail_postfix = get_mail_fomat(3)
    mail_subject = get_mail_fomat(4)
    #mail_content = get_mail_fomat(5)
    mail_content = content_list
    mail_name = get_mail_fomat(5)

    for i in mailto_list:
        if send_mail(i,mail_subject,mail_content,mail_host,mail_user,mail_pass,mail_postfix,mail_name):
            send_succeed_num +=1
            print "%s-->发送成功"%i
        else:
            send_fail_num +=1
            print "%s-->发送失败"%i
    print "\n-------------发送成功%d条" %send_succeed_num
    print "\n-------------发送失败%d条" %send_fail_num


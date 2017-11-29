#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-28 21:34:20
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def email(email_list, content, subject='抽屉新热榜-用户注册'):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = formataddr(['抽屉新热榜', '379100129@qq.com'])
    msg['Subject'] = subject

    smtp_server = smtplib.SMTP('smtp.qq.com', 25) # smtp服务器地址和端口号
    smtp_server.login = ('379100129@qq.com', 'bin10bin29') # smtp邮箱用户名密码
    smtp_server.sendmail('379100129@qq.com', email_list, msg.as_string())
    smtp_server.quit()

def main():
    email(['38440156@qq.com'],'测试测试测试测试测试测试测试测试测试')

if __name__ == '__main__':
    main()
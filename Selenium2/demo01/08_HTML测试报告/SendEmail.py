#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import encoders


SERVER="smtp.agrithings.cn"  # 设置服务器
ME = 'gaoyanbin@agrithings.cn' # 自己的邮件名
REV_LIST = [
    'gaoyanbin@agrithings.cn',
]


class SendEmail:
    def __init__(self, projectName,fileName,pwd):
        self.pwd = pwd
        self.msg = MIMEMultipart()
        self.msg['Subject'] = Header(projectName + '-自动测试报告', 'utf-8')
        self.msg['From'] = ME
        self.msg['To'] = ";".join(REV_LIST)

        # 读取html文档的内容。
        with open(fileName, 'rb') as f:
            self.mail_body = f.read()
        att1 = MIMEText(self.mail_body, 'html', 'utf-8')
        self.msg.attach(att1)

        # 附件
        att2 = MIMEBase('application', 'octet-stream')
        att2.set_payload(open(fileName, 'rb').read())
        att2.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', fileName.split('\\')[-1]))
        encoders.encode_base64(att2) # 中文附件名
        self.msg.attach(att2)

    def send(self):
        smtp = smtplib.SMTP(port=25, timeout=30)
        smtp.connect(SERVER)
        smtp.login(ME, self.pwd)
        smtp.sendmail(self.msg['From'], self.msg['To'], msg=self.msg.as_string())
        smtp.quit()
        print('Email send out!')
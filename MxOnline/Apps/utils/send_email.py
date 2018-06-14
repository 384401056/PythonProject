#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Blueice'
__date__ = '2018/6/14 16:43'

from django.core import mail

from Apps.User.models import EmailVerifyRecord

import random
import string
from MxOnline import settings


def send_register_email(email_address, type = "register"):
    """
    发送注册邮件
    :param email_address: 邮箱地址
    :param type: 邮件类型
    :return:
    """

    # 生成邮箱验证码对象
    email_record = EmailVerifyRecord()
    email_record.code = generate_random_str()
    email_record.email = email_address
    email_record.send_type = type
    email_record.save()

    email_content = {}

    if type == "register":
        email_content['title'] = "MxOnline注册激活链接"
        email_content['body'] = "请点击以下链接，激活你的账号：http://127.0.0.1:8000/active{0}".format(email_record.code)

        # 通过django来发送邮件
        send_status = mail.send_mail(
            subject=email_content['title'], # 邮件标题
            message=email_content['body'], # 邮件内容
            from_email= settings.EMAIL_FROM, # 发送人
            recipient_list=[email_address,] # 接收人列表
        )

        if send_status:
            print("send email succes!")
        else:
            print("send email faild...")


def generate_random_str(random_length=20):
    """
    生成随机字符串
    :param random_length: 指定长度
    :return:
    """
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, random_length))
    return ran_str


if __name__ == '__main__':
    pass

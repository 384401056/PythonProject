#!/usr/bin/env python
# -*- coding utf-8 -*-
import hashlib


def md5(pwd):
    '''对密码进行MD5加密'''
    hashmd5 = hashlib.md5(bytes('加盐', encoding='utf-8'))  # 加盐
    hashmd5.update(bytes(pwd, encoding='utf-8'))
    return hashmd5.hexdigest()


def register(user, pwd):
    '''用户注册，如果用户名存在则返回'''
    isExist = False
    with open('db', 'r', encoding='utf-8') as f:
        for line in f:
            u, p = line.strip().split('|')
            if u == user:
                print('用户已经存在!')
                isExist = True

    if not isExist:
        with open('db', 'a+', encoding='utf-8') as f:
            f.write('%s|%s\n' % (user, md5(pwd)))
            print('注册成功')


def login(user, pwd):
    '''用户登录'''

    isExist = False
    with open('db', 'r', encoding='utf-8') as f:
        for line in f:
            u, p = line.strip().split('|')
            if u == user:
                isExist = True
                if md5(pwd) == p:
                    print('登录成功')
                else:
                    print('登录失败!')
        if not isExist:
            print('用户不存在!')


def main():
    i = input('1. 注册, 2.登录 ')
    if i == '1':
        user = input('用户名：')
        pwd = input('密码：')
        register(user, pwd)
    elif i == '2':
        user = input('用户名：')
        pwd = input('密码：')
        login(user, pwd)
    else:
        print('输入错误!')


if __name__ == '__main__':
    main()

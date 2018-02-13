#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-13 22:30:36
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import hashlib


def testPasswd(cryptPasswd):
    # 把口令中的前两个字符取出，做为盐。
    # salt = cryptPasswd[0:2]
    with open('dictionary.txt', 'r') as dictFile:
        for word in dictFile.readlines():
            word = word.strip('\n')
            digest = hashlib.sha512(word.encode('utf-8')).hexdigest()
            if cryptPasswd == digest:
                print('[+] Found Password: %s' % word)
                return
    print('[-] Password Not Found.')


def main():
    with open('passwords.txt', 'r') as pwdFile:
        for password in pwdFile.readlines():
            password = password.strip('\n')
            testPasswd(password)


# def createDictionary():
#     try:
#         with open('dictionary.txt', 'r') as oldFile, open('passwords.txt', 'w') as newFile:
#             for word in oldFile.readlines():
#                 word = word.strip('\n')
#
#                 # 对字符进行加密码（sha512）
#                 hash = hashlib.sha512(word.encode('utf-8'))
#                 salt = hash.hexdigest()[0:2]  # 从原生的sha码上取盐。
#                 hash.update(salt.encode('utf-8'))  # 加盐操作.
#                 finalpwd = hash.hexdigest()  # 最终的sha码.
#
#                 newFile.write(finalpwd + '\n')
#     except Exception as ex:
#         print(ex)
#     return


# import crypt   #导入crypt模块
# import time
# start_time = time.time()   #计时器
# src="XXXXXXX:$6$H82h.4w0$9/1OII6XNiyvKCJBv3.xxxxxxxxxxxxxxxxxlFEs.tJUpWQlObHIj32WSe/RYsgK9l07LkpGZTIr2s1fRSQ8Rr/:16003:0:99999:7:::"   #从/etc/shadow所得
# username=src.split(":",1)[0]     #以冒号分割，分成两部分，得到一个列表，取第一部分
# lst=src.split(":",2)[1]      #以冒号分割，分成两部分，得到一个列表，取第二部分即加密之后的密码字符串
# start_index=lst.find("$")    #找到第一个“$”出现的索引
# finish_index=lst.rfind("$")  #找到最后一个“$”出现的索引
# salt=lst[start_index:finish_index+1]    #两个$之间的为盐
# dic=["a",'b','c', 'd', 'admin', 'c','xxxxxxxxx']    #字典
# for word in dic:
#     if crypt.crypt(word,salt) == lst:
#         print "I find it:" + word
#         print "The username is:"+username
#         break
# else:
#     print "serching is failed"    #这里用到了for else.如果是以break退出的，说明找到了密码，则不会执行else.如果没有找到密码，遍历结束后执行else语句（只执行一次，若写在for里面，则每次遍历一个元素执行一次else）。
# print time.time()-start_time


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import crypt

'''
通过Unitx系统下的 /etc/shadow 文件，进行与字典文件之间的加密字符对比。来破解出用户密码。
'''

def testPasswd(cryptPass):
    # 把口令中的$中间的字符取出，做为盐。
    start_index = cryptPass.find("$")  # 找到第一个“$”出现的索引
    finish_index = cryptPass.rfind("$")  # 找到最后一个“$”出现的索引
    salt = cryptPass[start_index:finish_index + 1]  # 两个$之间的为盐
    with open('dictionary.txt', 'r') as dictFile:
        for word in dictFile.readlines():
            word = word.strip('\n')
            # 对字典中的数据进行加盐加密。
            cryptWord = crypt.crypt(word, salt)

            # 如果字典中的加密字符与输入的密码相等，则说明密码一致。
            if cryptWord == cryptPass:
                print('[+] Found Password: %s' % word)
                return
    print('[-] Password Not Found.')
    return


def main():
    with open('passwords.txt', 'r') as passFile:
        for line in passFile.readlines():
            user = line.split(':',1)[0]
            cryptPass = line.split(':',2)[1].strip(' ')
            print('[*] Cracking Password For:%s' % user)
            testPasswd(cryptPass)


if __name__ == '__main__':
    main()

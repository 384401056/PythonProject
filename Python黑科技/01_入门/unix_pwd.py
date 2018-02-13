#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import crypt


def testPasswd(cryptPass):
    # 把口令中的前两个字符取出，做为盐。
    salt = cryptPass[0:2]
    with open('dictionary.txt', 'r') as dictFile:
        for word in dictFile.readlines():
            word = word.strip('\n')
            cryptWord = crypt.crypt(word, salt)

            if cryptWord == cryptPass:
                print('[+] Found Password: %s' % word)
                return
            else:
                print('cryptPass:', cryptPass)
                print('cryptWord:', cryptWord)
    print('[-] Password Not Found.')
    return


def main():
    with open('passwords.txt', 'r') as passFile:
        for line in passFile.readlines():
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print('[*] Cracking Password For:%s' % user)
            testPasswd(cryptPass)


if __name__ == '__main__':
    main()

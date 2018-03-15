#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
import random

def random_code():
    return random.randrange(100000,999999)

def generate_md5(value):
    pass



def main():
    print(random_code())

if __name__ == '__main__':
    main()
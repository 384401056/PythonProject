#!/usr/bin/env python
# -*- coding utf-8 -*-

import sys, time

'''需要在cmd中运行此脚本才有效果'''
for i in range(31):
    # 打印之前清空屏幕
    sys.stdout.write('\r')
    # 打印出百分比，和多个#
    sys.stdout.write('%s %% | %s' % (int(i/30*100), int(i/30*100)*'#'))
    sys.stdout.flush()
    time.sleep(0.1)

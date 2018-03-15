#!/usr/bin/env python
# -*- coding utf-8 -*-
import subprocess

def main():
    ret = subprocess.check_output(['dir'], shell=True)
    print(str(ret, encoding='gbk'))


if __name__ == '__main__':
    main()
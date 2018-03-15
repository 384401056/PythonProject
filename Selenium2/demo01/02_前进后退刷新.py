#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.baidu.com") # 只有界面全部加载完毕后才会向下执行。
    time.sleep(3)
    driver.get("https://news.baidu.com")
    time.sleep(3)
    driver.back() # 回到上一页
    time.sleep(3)
    driver.forward() # 回到下一页
    driver.refresh() # 刷新当前页

if __name__ == '__main__':
    main()
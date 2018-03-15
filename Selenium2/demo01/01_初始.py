#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    driver = webdriver.Firefox()
    # driver.maximize_window()

    driver.get("https://www.baidu.com")

    # driver.find_element_by_xpath('//*[@id="kw"]').send_keys('Python')
    # driver.find_element_by_xpath('//*[@id="su"]').click()


    driver.find_element_by_id('kw').send_keys('Selenium2')
    driver.find_element_by_id('su').click()

    # driver.find_element(By.ID, 'kw').send_keys('Selenium2')
    # driver.find_element(By.ID, 'su').click()

    driver.set_window_size(480, 800) # 如果窗口缩的太小，可能会无法点击按钮。
    # driver.quit()


if __name__ == '__main__':
    main()

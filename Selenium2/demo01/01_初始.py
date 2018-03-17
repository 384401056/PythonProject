#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webself.driver
from selenium.webself.driver.common.by import By

def main():
    self.driver = webself.driver.Firefox()
    # self.driver.maximize_window()

    self.driver.get("https://www.baidu.com")

    # self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('Python')
    # self.driver.find_element_by_xpath('//*[@id="su"]').click()


    self.driver.find_element_by_id('kw').send_keys('Selenium2')
    self.driver.find_element_by_id('su').click()

    # self.driver.find_element(By.ID, 'kw').send_keys('Selenium2')
    # self.driver.find_element(By.ID, 'su').click()

    self.driver.set_window_size(480, 800) # 如果窗口缩的太小，可能会无法点击按钮。
    # self.driver.quit()


if __name__ == '__main__':
    main()

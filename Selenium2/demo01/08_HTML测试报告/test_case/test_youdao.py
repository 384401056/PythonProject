#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest
import time


class YoudaoTest(unittest.TestCase):
    '''有道测试'''
    def setUp(self):
        print('MyTest start.')
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10) # 设置调用的超时时间
        self.driver.get("https://www.youdao.com")

    def test_youdao(self):
        '''有道翻译测试'''
        try:
            self.driver.find_element_by_id('query').clear()# 错误代码
            self.driver.find_element_by_id('translateContent').send_keys('WebDriver')
            self.driver.find_element_by_xpath('/html/body/div[5]/div/form/button').click()
            time.sleep(2)
            # self.driver.get_screenshot_as_file('.\\reports\\youdao_search.jpg')
            # print(self.driver.title) # web页面的title显示文字
        except Exception as e:
            print(e)
            # self.driver.get_screenshot_as_file('.\\reports\\youdao_error.jpg')
        finally:
            self.driver.close()

    def tearDown(self):
        print('MyTest end.')


if __name__ == "__main__":
    unittest.main()

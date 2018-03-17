#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest
import time


class BaiduTest(unittest.TestCase):
    '''百度测试'''
    def setUp(self):
        print('MyTest start.')
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10) # 设置调用的超时时间
        self.driver.get("https://www.baidu.com")

    def test_baidu(self):
        '''百度搜索测试'''
        try:
            self.driver.find_element_by_id('kw').send_keys('Selenium2')
            self.driver.find_element_by_id('su').click()
            time.sleep(2)
            # self.driver.get_screenshot_as_file('.\\reports\\baidu_search.jpg')
            # print(self.driver.title) # web页面的title显示文字
            # self.assertEqual(self.driver.title, 'Selenium2_百度搜索')
        except Exception as e:
            print(e)
            # self.driver.get_screenshot_as_file('.\\reports\\baidu_error.jpg')
        finally:
            self.driver.close()

    def tearDown(self):
        print('MyTest end.')


if __name__ == "__main__":
    unittest.main()

# coding:utf-8
import re
import time
import json
from datetime import datetime
from bs4 import BeautifulSoup
import lxml.html
import lxml.cssselect

def main():
    data_list = read_file('data_list.json')["data_list"]
    lxml_parse(data_list[0]["html"])




def lxml_parse(html):
    '''使用lxml进行网页的解析'''
    # 对html进行修复操作
    tree = lxml.html.fromstring(html)
    lxml.html.tostring(tree, pretty_print=True)

    # 抓取html中的面积数据
    td = tree.cssselect('tr#places_area__row > td.w2p_fw')[0]
    area = td.text_content()
    print area



def beautifulsoup_parse(html):
    '''使用BeautifulSoup进行网面的解析'''
    # 对html进行修复操作
    soup = BeautifulSoup(html, 'html.parser')
    soup.prettify()

    # 抓取html中的面积数据
    tr = soup.find(attrs={'id': 'places_area__row'})
    td = tr.find(attrs={'class': 'w2p_fw'})
    area = td.text
    print area


def re_parse(html):
    '''使用正则式表达式进行解析'''
    # 抓取html中的面积数据
    area = re.search('<tr id="places_area__row">.*?<td class="w2p_fw">(.*?)</td>',html).groups()[0]
    print area



def read_file(fileName):
    '''从json文件中读取数据，并返回字典对象'''
    with open(fileName, 'r') as fo:
        return json.load(fo,'utf-8')


if __name__ == '__main__':
    main()
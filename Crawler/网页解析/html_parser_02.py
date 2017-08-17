# coding:utf-8
import re
import time
import json
from datetime import datetime
from bs4 import BeautifulSoup
import lxml.html
import lxml.cssselect


FIELDS = ('area','population','iso','country',
          'capital','continent','tld','currency_code',
          'currency_name','phone','postal_code_format',
          'postal_code_regex','languages','neighbours')

result = {}
country_data=[]
def main():

    data_list = read_file('data_list.json')["data_list"]

    for data in data_list:
        html = data["html"]
        for field in FIELDS:
            value = lxml_parse(html, field)
            result[field] = value
        country_data.append(result)
    print json.dumps({"data_lsit":country_data})


def lxml_parse(html, field):
    '''使用lxml进行网页的解析'''
    # 对html进行修复操作
    tree = lxml.html.fromstring(html)
    lxml.html.tostring(tree, pretty_print=True)

    # 抓取html中的面积数据
    td = tree.cssselect('tr#places_%s__row > td.w2p_fw'% field)[0]
    return td.text_content()



def beautifulsoup_parse(html, field):
    '''使用BeautifulSoup进行网面的解析'''
    # 对html进行修复操作
    soup = BeautifulSoup(html, 'html.parser')
    soup.prettify()

    # 抓取html中的面积数据
    tr = soup.find(attrs={'id': 'places_%s__row'% field})
    td = tr.find(attrs={'class': 'w2p_fw'})
    return td.text


def re_parse(html, field):
    '''使用正则式表达式进行解析'''
    # 抓取html中的面积数据
    partten = '<tr id="places_%s__row">.*?<td class="w2p_fw">(.*?)</td>'% field
    return re.search(partten, html).groups()[0]



def read_file(fileName):
    '''从json文件中读取数据，并返回字典对象'''
    with open(fileName, 'r') as fo:
        return json.load(fo,'utf-8')


if __name__ == '__main__':
    main()
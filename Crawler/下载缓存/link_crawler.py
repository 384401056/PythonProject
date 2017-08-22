# coding:utf-8
import re
import urlparse
import urllib2
import time
from datetime import datetime
import json
import Queue
import csv
import lxml.html
import lxml.cssselect
from Downloader import Downloader
from Write_to_csv import Write_to_csv
from Write_to_mongo import Write_to_mongo

data_list = []
def link_crawler(seed_url, link_regex=None, delay=3, max_depth=-1, max_urls=-1, headers=None, user_agent='wswp',
                 proxy=None, num_retries=1, callback=None):

    """Crawl from the given seed URL following links matched by link_regex"""
    crawl_queue = Queue.deque([seed_url])
    seen = {seed_url: 0}
    num_urls = 0

    # 创建下载对象
    downloader = Downloader(delay=delay, user_agent=None, proxies=None, num_retries=num_retries)
    # 创建保存为csv的对象
    write_to_csv = Write_to_csv('cache_html.csv',['code','html'])
    # 创建保存为文档数据的对象
    write_to_mongo = Write_to_mongo('127.0.0.1', 27017, 'cache', 'html')

    while crawl_queue:
        url = crawl_queue.pop()
        # 下载网页
        down_result = downloader(url)

        # 从下载下载结果中获取html
        html = down_result['html']

        links = []
        # 保存 /view 的数据.
        if re.match(seed_url + '/places/default/(view)', url):
            # 保存下载结果
            row = [down_result['code'], down_result['html']]
            write_to_csv(row)
            write_to_mongo(down_result)

            # data_list.append(down_result)

            # 通过回调函数来解析html
            if callback:
                callback(html)

        depth = seen[url]
        if depth != max_depth:
            # can still crawl further
            if link_regex:
                # filter for links matching our regular expression
                links.extend(link for link in get_links(html) if re.match(link_regex, link))

            for link in links:
                link = normalize(seed_url, link)
                # check whether already crawled this link
                if link not in seen:
                    seen[link] = depth + 1
                    # check link is within same domain
                    if same_domain(seed_url, link):
                        # success! add this new link to queue
                        crawl_queue.append(link)
            print len(crawl_queue)

        num_urls += 1
        if num_urls == max_urls:
            break

        # 将结果输出到json文件
        # write_to_file(data_list)

def normalize(seed_url, link):
    """Normalize this URL by removing hash and adding domain
    """
    link, _ = urlparse.urldefrag(link)  # remove hash to avoid duplicates
    return urlparse.urljoin(seed_url, link)


def same_domain(url1, url2):
    """Return True if both URL's belong to same domain
    """
    return urlparse.urlparse(url1).netloc == urlparse.urlparse(url2).netloc


def get_links(html):
    """Return a list of links from html
    """
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)

def write_to_file(data_list):
    with open('data_list.json','wb') as fo:
        # 字典以json格式写入文件.
        json.dump({'data_list':data_list}, fo)
        # fo.write(str({'data_list':data_list}))

class ScrapCallback:
    ''' 将html数据解析后存为.csv文件 '''
    def __init__(self):
        # 创建csv文件，并写入表头字段,打开方式用a+时，写入到csv中会存在一行间一行的问题。
        # 将打开的方法改为ab+，就不存在这个问题了.
        with open('conutries.csv', 'wb')as fo:
            csv_writer = csv.writer(fo)
            # self.file = csv.writer(open('conutries.csv','ab+'))
            self.fields = ('area','population','iso','country',
              'capital','continent','tld','currency_code',
              'currency_name','phone','postal_code_format',
              'postal_code_regex','languages','neighbours')
            csv_writer.writerow(self.fields)

    def __call__(self, html):
        row = []
        try:
            for field in self.fields:
                tree = lxml.html.fromstring(html)
                lxml.html.tostring(tree, pretty_print=True)
                td = tree.cssselect('tr#places_%s__row > td.w2p_fw' % field)[0]
                row.append(td.text_content())
            # 写入到csv中会存在一行间一行的问题。将打开的方法改为改为二进度模式，就不存在这个问题了.
            with open('conutries.csv', 'ab+')as fo:
                csv_writer = csv.writer(fo)
                csv_writer.writerow(row)
        except lxml.etree.XMLSyntaxError as e:
            print e.reason




if __name__ == '__main__':
    link_crawler('http://example.webscraping.com', '/places/default/(index|view)', delay=3, num_retries=1, callback=ScrapCallback())
    # link_crawler('http://example.webscraping.com', '/(index|view)', delay=0, num_retries=1, max_depth=1,user_agent='GoodCrawler')


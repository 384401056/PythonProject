# coding=utf-8

import urllib2
import re

def download(url, user_agent = 'wswp', re_times = 2 ):
    '''可以设置用户代理的下载方法'''
    print 'DownLoad....'
    # 设置请求头
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers = headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print "DownLoad Error: ", e.reason
        html = None
        if re_times > 0:
            print '重试次数: ', re_times
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, user_agent, re_times - 1)
    return html


def crawl_sitemap(url):
    sitemap = download(url)

    links = re.findall('<loc>(.*?)</loc>', sitemap)

    for link in links:
        html = download(link)
        # ....
        # ....

print download('http://example.webscraping.com/sitemap.xml')
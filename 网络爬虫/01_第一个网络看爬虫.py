# coding=utf-8

import urllib2

def download01(url):
    '''下载网页'''
    print 'DownLoad....'
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'DownLoad Error:', e.reason
        html = None
    return html


def download02(url, re_times = 2):
    '''支持重试下载网页的新版本'''
    print 'DownLoad....'
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print "DownLoad Error: ", e.reason
        html = None
        if re_times > 0:
            print '重试次数: ', re_times
            # 如果错误信息e中有code属性，并且e.code在500和600之间。
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # 递归调用,并把重试次数减1.
                return download02(url, re_times - 1)
    return html



def download03(url, user_agent = 'wswp', re_times = 2 ):
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
                return download03(url, user_agent, re_times - 1)
    return html



def main():
    print download01('https://www.baidu.com')
    # download02('http://httpstat.us/500', 2)
    # print download03('http://example.webscraping.com/')


if __name__ == '__main__':
    main()
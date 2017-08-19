# coding=utf-8
import urllib2
import itertools


def download(url, user_agent = 'wswp', re_times = 2 ):
    '''可以设置用户代理的下载方法'''
    print 'DownLoad....', url
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
            if hasattr(e, 'code') and 400 <= e.code < 600:
                return download(url, user_agent, re_times - 1)
            else:
                print e.code
    return html


def id_crawler():
    '''ID遍历爬虫'''
    list_html = []
    # 从1开始至无穷大
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/places/default/view/-%d' % page
        html = download(url)
        if html is None:
            break
        else:
            text = {"url":url, 'html':html}
            list_html.append(text)
            print url

    # 将抓取内容写入数据
    with open('html.csv','w') as fo:
        fo.write(str({'data':list_htmllist_html}))



if __name__ == '__main__':
    id_crawler()
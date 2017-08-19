# coding=utf-8
import urllib2
import re
import urlparse
import Throttle

# 设置下载限速(秒)
throttle = Throttle.Throttle(5)
data_list = []

def download(url, user_agent = 'wswp', proxy=None, re_times = 2):
    '''可以设置用户代理的下载方法'''
    print 'DownLoad....', url

    # 限制下载速度
    throttle.wait(url)

    # 设置请求头
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers = headers)

    opener = urllib2.build_opener()
    # 添加代理的支持
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html = opener.open(request).read()
        # html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print "DownLoad Error: ", e.reason
        html = None
        if re_times > 0:
            print '重试次数: ', re_times
            if hasattr(e, 'code') and 400 <= e.code < 600:
                return download(url, user_agent, proxy, re_times - 1)
            else:
                print e.code
    except BaseException as be:
        print be.reason

    return html


def link_crawler(base_url, link_regex):
    '''链接爬虫,传入网站和链接的正则表达式'''

    craw_queue = [base_url]
    seen = set(craw_queue) # 将链接队列转为集合,可以消除重复的链接

    while craw_queue:

        # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
        url = craw_queue.pop()
        html = download(url)
        if re.match(urlparse.urljoin(base_url, '/places/default/view'),url):
            print '这是数据页面..'
            data = {'url':url,'html':html}
            data_list.append(data)
        link_list = get_links(html)

        # 从html中获取子链接
        for link in link_list:
            # 如果子链接与传入的正则相匹配就加入链接队列
            if re.match(link_regex,link):
                # 将相对路径变为绝对路径.
                link = urlparse.urljoin(base_url, link)
                # 如果完整的链接地址与原来有的不重复就加入队列
                if link not in seen:
                    seen.add(link)
                    craw_queue.append(link)
    writToFile(data_list)

def writToFile(data):
    '''将抓取内容写入数据'''
    with open('data.json', 'a+') as fo:
        fo.write(str({'datalist':data_list}))



def get_links(html):
    ''''获取每个html页面中的超链接,但是这些链接都是相对链接'''
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html) # 返回的是一个链接列表

def main():
    # 传入地址和正则，其中index是翻页的,view是详情页面.
    link_crawler('http://example.webscraping.com/', '/places/default/(index|view)')


if __name__ == '__main__':
    main()
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


data_list = []

def link_crawler(seed_url, link_regex=None, delay=5, max_depth=-1, max_urls=-1, headers=None, user_agent='wswp',
                 proxy=None, num_retries=1, callback=None):
    """Crawl from the given seed URL following links matched by link_regex"""
    # the queue of URL's that still need to be crawled
    crawl_queue = Queue.deque([seed_url])
    # the URL's that have been seen and at what depth
    seen = {seed_url: 0}
    # track how many URL's have been downloaded
    num_urls = 0

    throttle = Throttle(delay)
    headers = headers or {}
    if user_agent:
        headers['User-agent'] = user_agent

    while crawl_queue:
        url = crawl_queue.pop()
        # check url passes robots.txt restrictions
        throttle.wait(url)
        html = download(url, headers, proxy=proxy, num_retries=num_retries)
        links = []

        # 保存 /view 的数据.
        if re.match(seed_url + '/places/default/(view)', url):
            data_list.append({"url":url, "html":html})
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
        # check whether have reached downloaded maximum
        num_urls += 1
        if num_urls == max_urls:
            break

        # 保存html内容到json文件
        write_to_file(data_list)



def download(url, headers, proxy, num_retries, data=None):
    print 'Downloading:', url
    request = urllib2.Request(url, data, headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        response = opener.open(request)
        html = response.read()
        code = response.code
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = ''
        if hasattr(e, 'code'):
            code = e.code
            if num_retries > 0 and 500 <= code < 600:
                # retry 5XX HTTP errors
                return download(url, headers, proxy, num_retries - 1, data)
        else:
            code = None
    return html


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


class Throttle:
    """Throttle downloading by sleeping between requests to same domain"""
    def __init__(self, delay):
        # amount of delay between downloads for each domain
        self.delay = delay
        # timestamp of when a domain was last accessed
        self.domains = {}

    def wait(self, url):
        domain = urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)

        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.now()


if __name__ == '__main__':
    link_crawler('http://example.webscraping.com', '/places/default/(index|view)', delay=2, num_retries=1)
    # link_crawler('http://example.webscraping.com', '/places/default/(index|view)', delay=3, num_retries=1, callback=ScrapCallback())
    # link_crawler('http://example.webscraping.com', '/(index|view)', delay=0, num_retries=1, max_depth=1,user_agent='GoodCrawler')
# coding:utf-8
import Queue
import csv
import lxml.html
import lxml.cssselect
from Downloader import Downloader

'''下载Alex排行榜前2000的网站地址'''

# data_list = []
def link_crawler(seed_url, link_regex=None, delay=3, headers=None, user_agent='wswp', proxy=None, num_retries=1, callback=None):

    crawl_queue = Queue.deque([seed_url])

    # 生成因定链接
    for i in range(2,101):
        crawl_queue.append(seed_url+str(i))

    # 创建下载对象
    downloader = Downloader(delay=delay, user_agent=None, proxies=None, num_retries=num_retries)

    while crawl_queue:
        url = crawl_queue.pop()
        # 下载网页
        down_result = downloader(url)
        # 从下载下载结果中获取html
        html = down_result['html']

        # 解析网页
        if callback:
            callback(html)

        print len(crawl_queue)


class Alax_Callback:
    ''' 将html数据解析后存为.csv文件 '''
    def __init__(self):
        # 创建csv文件，并写入表头字段,打开方式用a+时，写入到csv中会存在一行间一行的问题。
        # 将打开的方法改为ab+，就不存在这个问题了.
        with open('alex.csv', 'wb')as fo:
            csv_writer = csv.writer(fo)
            self.fields = ('rank-index', 'info-wrap')
            csv_writer.writerow(self.fields)

    def __call__(self, html):
        try:
            # for field in self.fields:
            tree = lxml.html.fromstring(html)
            lxml.html.tostring(tree, pretty_print=True)
            rank_index = tree.cssselect('ul.siterank-sitelist > li > div.rank-index')
            info_wrap = tree.cssselect('ul.siterank-sitelist > li > div.info-wrap >div.domain > a')
            # 写入到csv中会存在一行间一行的问题。将打开的方法改为改为二进度模式，就不存在这个问题了.
            with open('alex.csv', 'ab+')as fo:
                for index in range(len(rank_index)):
                    row = []
                    row.append(rank_index[index].text_content())
                    row.append('www.%s'% info_wrap[index].text_content().lower())
                    csv_writer = csv.writer(fo)
                    csv_writer.writerow(row)
        except lxml.etree.XMLSyntaxError as e:
            print e.reason


def main():
    link_crawler('http://www.alexa.cn/siterank/', delay=2, callback=Alax_Callback())


if __name__ == '__main__':
    main()
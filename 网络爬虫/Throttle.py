# coding=utf-8
import urlparse
import datetime
import time


class Throttle:
    ''' 在两次下载之间添加迟时 '''
    def __init__(self, delay):
        self.delay = delay
        self.domains = {}


    def wait(self, url):
        # 获取url的网络域名
        domain = urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)

        if self.delay > 0 and last_accessed is not None:
            # 如果 限速时间 大于 （当前时间 - 最后一次下载时间，就sleep他们之间的秒差.
            t = (datetime.datetime.now() - last_accessed).seconds
            sleep_secs = self.delay - t

            if sleep_secs > 0 :
                print 'sleep.....'
                time.sleep(sleep_secs)

        # 设置当前时间为某个域名的时间
        self.domains[domain] = datetime.datetime.now()


def main():
    th = Throttle(20)
    for i in range(4):
        th.wait('http://example.webscraping.com/view/index.html')


if __name__ == '__main__':
    main()
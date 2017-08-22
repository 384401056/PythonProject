# coding:utf-8
import random
import urlparse
import urllib2
from Throttle import Throttle

class Downloader:

    def __init__(self, delay=5, user_agent='wswp',
                 proxies=None, num_retries=1, cache = None):
        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxies = proxies
        self.num_retries = num_retries
        self.cache = cache

    def __call__(self, url):
        '''对象被直接调用时执行'''
        # 延时下载
        self.throttle.wait(url)
        # 如果代理列表不为空则随机返回一个代理地址
        proxy = random.choice(self.proxies) if self.proxies else None
        headers = {'User-agent':self.user_agent}
        return self.download(url, headers, proxy, self.num_retries)

    def download(self, url, headers, proxy, num_retries, data=None):
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
                    return self.download(url, headers, proxy, num_retries - 1, data)
            else:
                code = None
        return {'code':code, 'html':html}


if __name__ == '__main__':
    pass

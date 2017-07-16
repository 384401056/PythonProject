from atexit import register
from threading import Thread
from time import ctime, sleep
from re import compile
from urllib import request


''' 图书排名示例_01'''


# 匹配#和数字的组合,
pattern = compile('#([\d,]+) in Books ')
AMZN = 'https://www.amazon.com/dp/'
ISBNs = {
    '0132269937':'Core Python Programming',
    '0132356139':'Python Web Development with Django',
    '0137143419':'Python Fundamentals LiveLessons'
}

def getRanking(isbn):
    # 返回一个文件
    pageFile = request.urlopen('%s%s' % (AMZN,isbn))
    data = pageFile.read()
    pageFile.close()
    return pattern.findall(data.decode())[0] # 从网页文件中匹配Amazon商品图书排名的模式

def _showRanking(isbn):
    # %r 字符串 (采用repr()的显示)
    print('- %s ranked %s' % (ISBNs[isbn], getRanking(isbn)))



def main():
    print('At ', ctime(), 'on Amazon...', )
    for isbn in ISBNs:
        Thread(target=_showRanking,args=(isbn,)).start() # 使用多线程可节省执行时间
        # _showRanking(isbn)

@register
def _atexit():
    ''' 这个方法使用了装饰器,在Python 解释器中注册一个退出函数，也就是说，它会在脚本退出之前请求调用这个特殊函数。
    （ 如果不使用装饰器的方式， 也可以直接使用register(_atexit())）。
    '''
    print('all done at', ctime())

if __name__ == '__main__':
    main()


''' 图书排名示例_01 多线程版本 '''

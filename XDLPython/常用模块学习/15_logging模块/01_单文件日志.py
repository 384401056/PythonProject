#!/usr/bin/env python
# -*- coding utf-8 -*-

import logging


def main():
    logging.basicConfig(
        filename='log.log',
        format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s', # 时间 用户名 日志级别 模块名(文件) ：信息
        datefmt='%Y-%m-%d %H:%M:%S %p',
        level=10
    )

    ''' 日志级别的定义
        CRITICAL = 50
        FATAL = CRITICAL
        ERROR = 40
        WARNING = 30
        WARN = WARNING
        INFO = 20
        DEBUG = 10
        NOTSET = 0
    '''

    logging.debug('debug')
    logging.info('info')
    logging.warning('warning')
    logging.error('error')
    logging.critical('critical')

    # 自定义级别，并输出日志。
    logging.log(10, 'log')




if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding utf-8 -*-

import logging


def main():
    # 定义文件及其格式
    file_1_1 = logging.FileHandler('l_1.log', 'a', encoding='utf-8')
    fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s -%(filename)s -%(funcName)s:  %(message)s")
    file_1_1.setFormatter(fmt)

    file_1_2 = logging.FileHandler('l_2.log', 'a', encoding='utf-8')
    fmt = logging.Formatter()
    file_1_2.setFormatter(fmt)

    # 定义日志
    logger1 = logging.Logger('s1', level=logging.NOTSET)
    logger1.addHandler(file_1_1)
    logger1.addHandler(file_1_2)

    # 写日志
    logger1.debug('debug')
    logger1.info('info')
    logger1.warning('warning')
    logger1.error('error')
    logger1.critical('critical')


if __name__ == '__main__':
    main()
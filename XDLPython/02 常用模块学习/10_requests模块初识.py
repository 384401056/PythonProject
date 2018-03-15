#!/usr/bin/env python
# -*- coding utf-8 -*-

import requests


def main():
    response = requests.get('http://www.weather.com.cn/data/sk/101110101.html')
    response.encoding = 'utf-8'
    result = response.text
    print(result)


if __name__ == '__main__':
    main()

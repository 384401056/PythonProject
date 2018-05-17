#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import split, splitext


class MyAdapter(object):
    """
    适配器类
    """
    def __init__(self, filename):
        self.filename = filename

    @property
    def title(self):
        return splitext(split(self.filename)[-1])[0]

    @property
    def language(self):
        return('en')

    def __getitem__(self, item):
        return getattr(self, item, 'Unkown...')

class CoreInfo(object):
    def summary(self, dc_dict):
        print('Title: %s' % dc_dict['title'])
        print('Creator: %s' % dc_dict['Creator'])
        print('language: %s' % dc_dict['language'])



def main():
    adapter = MyAdapter('example.txt')
    infos = CoreInfo()
    infos.summary(adapter)

    print('-----------------------')
    print(adapter['title'])
    print(adapter['language'])
    print(adapter['Creator'])


if __name__ == '__main__':
    main()
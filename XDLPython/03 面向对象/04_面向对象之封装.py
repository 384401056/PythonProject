#!/usr/bin/env python
# -*- coding utf-8 -*-

class Oldboy:
    def fetch(self):
        print('fetch')
        print(self.backend)

    def add_record(self):
        print('add_record')
        print(self.backend)

    def del_record(self):
        print('del_record')
        print(self.backend)


def main():
    obj1 = Oldboy()
    obj1.backend = 'this is backend'  # 在对象中封装了一个变量.

    obj1.fetch()
    obj1.add_record()
    obj1.del_record()


if __name__ == '__main__':
    main()

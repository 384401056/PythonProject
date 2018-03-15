#!/usr/bin/env python
# -*- coding utf-8 -*-

class Oldboy:

    def fetch(self, backend):
        print(self)
        print(backend)
        self.add_record()


    def add_record(self):
        print('kkk')


def main():
    obj1 = Oldboy()
    print(obj1)
    obj1.fetch('obj1')

    obj2 = Oldboy()
    print(obj2)
    obj2.fetch('obj2')


if __name__ == '__main__':
    main()

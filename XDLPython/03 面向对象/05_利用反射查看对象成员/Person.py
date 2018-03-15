#!/usr/bin/env python
# -*- coding utf-8 -*-


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print('name: %s' % self.name)
        print('age: %d' % self.age)


def main():
    pass


if __name__ == '__main__':
    main()

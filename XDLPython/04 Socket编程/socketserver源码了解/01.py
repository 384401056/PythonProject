#!/usr/bin/env python
# -*- coding utf-8 -*-

class Person():

    def __init__(self):
        pass


    def handle(self):
        print('handle')
        print(self)

def main():
    print(Person())
    Person().handle()


if __name__ == '__main__':
    main()
#!/usr/bin/env python
# -*- coding utf-8 -*-

def main():

    try:
        raise Exception("这是我自己抛出的导常")
    except Exception as e:
        print(e)



if __name__ == '__main__':
    main()
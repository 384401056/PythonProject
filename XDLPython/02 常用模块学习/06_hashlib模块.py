#!/usr/bin/env python
# -*- coding utf-8 -*-
import hashlib


def main():
    # ######## md5 ########
    hash = hashlib.md5()
    # hash = hashlib.md5(bytes('加盐', encoding='utf-8')) # 加盐
    hash.update(bytes('123', encoding='utf-8'))
    print(hash.hexdigest())
    print(hash.digest())

    ######## sha1 ########
    hash = hashlib.sha1()
    hash.update(bytes('123', encoding='utf-8'))
    print(hash.hexdigest())

    # ######## sha256 ########
    hash = hashlib.sha256()
    hash.update(bytes('123', encoding='utf-8'))
    print(hash.hexdigest())

    # ######## sha384 ########
    hash = hashlib.sha384()
    hash.update(bytes('123', encoding='utf-8'))
    print(hash.hexdigest())

    # ######## sha512 ########
    hash = hashlib.sha512()
    hash.update(bytes('123', encoding='utf-8'))
    print(hash.hexdigest())


if __name__ == '__main__':
    main()
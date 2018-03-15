#!/usr/bin/env python
# -*- coding: utf-8 -*-

b1 = bytearray("gaoyanbin".encode("utf8"))
b2 = bytearray([1,2,3,4,5])
print b1
print str(b2)
print ' '.join(hex(x) for x in b1)
# payload = bytearray(b'\x01\x02\x03\x04\x05\x06').decode('utf-8')
# payload = str(b)
# print payload
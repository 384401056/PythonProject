import re

mt = re.search('[abcdefg][1234567][!@#$%^&][:"|<>?+]','this sfas b3!? 3e22')

if mt:
    print(mt.group())
else:
    print("未找到匹配")

mt = re.match('\w+@\w+\.com', 'a@b.com')

if mt:
    print(mt.group())
else:
    print("未找到匹配")

mt = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
if mt:
    print(mt.group(1))
    print(mt.group(2))
    print(mt.groups())
else:
    print("未找到匹配")

mt = re.search(r'\bfd', 'end The fdsaf')
if mt:
    print(mt.group())
else:
    print("未找到匹配")

# findall() 将返回一个匹配的符串列表，如果没有匹配则返回[]
ls = re.findall(r'The','aThea eThet 2Thee')
print(ls)
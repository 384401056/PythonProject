import re

# mt = re.search('[abcdefg][1234567][!@#$%^&][:"|<>?+]','this sfas b3!? 3e22')
#
# if mt:
#     print(mt.group())
# else:
#     print("未找到匹配")

# mt = re.match('\w+@\w+\.com', 'a@b.com')
#
# if mt:
#     print(mt.group())
# else:
#     print("未找到匹配")

# mt = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
# if mt:
#     print(mt.group(1))
#     print(mt.group(2))
#     print(mt.groups())
# else:
#     print("未找到匹配")

# mt = re.search(r'\bfd', 'end The fdsaf')
# if mt:
#     print(mt.group())
# else:
#     print("未找到匹配")

# findall(partten,string) 将返回一个匹配的符串列表，如果没有匹配则返回[]
# ls = re.findall(r'The','afThea aaeThet 322Thee')
# print(ls)
#
# # pattern = r'(th\w+)' # 查找以th开头,并且其后至少有1个字符,不区分大小写。
# pattern = r'(\w*th\w*)' # 查找前后带有(也可不带)th的字符。
# ls = re.findall(pattern,'afThea aaeThet 322Thee threesew th', re.I)
# print(ls)
#
# # sub subn
# pattern = r'X'
# ls = re.sub(pattern,'Mr Smith:','Dear X : I\'m X') # 将字符串中的X替换成其它字符
# lx = re.subn(pattern,'Mr Smith:','Dear X : I\'m X X X' ) # 将字符串中的X替换成其它字符,返回一个替换数量
# print(ls)
# print(lx)



# split() 中使用正则表达式

# ls = re.split(r':','32,xyz:233.tt')
# ls = re.split(r',|:|\.','32,xyz:233.tt') # 多条件分割
# pattern = ', |(?= (?:\d{5}|[A-Z]{2})) '
# DATA = ('Mountain View, CA 94040',
#         'Sunnyvale, CA',
#         'Los Altos, 94023',
#         'Cupertino 95014',
#         'Palo Alto CA',)
#
# for each in DATA:
#     print(re.split(pattern,each))

pattern = r'(?i)th\w+' # 不区分大小写
ls = re.findall(pattern,'there Theopew '
                        'THEDFA ThisSS '
                        'agrithings')
print(ls)

pattern = r'(?im)(^th[\w ]+)' # 不区分大小写，并且可跨行查寻
ls = re.findall(pattern,""" This line is the first, another line, that line, it's the best """)
print(ls)

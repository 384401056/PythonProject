'''函数练习'''
'''1.定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值。'''
# def func(*nums):
#     max = nums[0]
#     min = nums[0]
#     for each in nums:
#         if isinstance(each,int):
#             if each > max:
#                 max = each
#             elif each < min:
#                 min = each
#         else:
#             return '输入的数据有误!'
#     return '最大值为: %d 　最小值为：%d' % (max ,min)
#
# print(func(87,2,3,43,432,432,432,123,32,43,25,485,'a',65))

# 第二种方法
# def func(*nums):
#     ls = list(nums)
#     for each in nums:
#         if not isinstance(each,int):
#             return '输入的数据有误! ' + str(each)
#     ls.sort() # 排序
#     return '最大值为: %d 　最小值为：%d' % (ls[0] ,ls[len(ls)-1])
# print(func(87,21,3,43,432,432,432,123,32.3,43,25,48500,65))

'''2.定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。'''
# def func(*strs):
#     length = 0
#     result = ''
#     for each in strs:
#         if isinstance(each,str):
#             if len(each) > length:
#                 length = len(each)
#                 result = each
#         else:
#             return '输入的数据有误!'
#
#     return '最长的字符串为：%s ' % result
#
# print(func('123',1,'gaoyanbin'))

# 第二种方式
# def func(*strs):
#     ls = list(strs)
#     for each in strs:
#         if not isinstance(each,str):
#             return '输入的数据有误!'
#     # 使用推导式，生成一个字典，key为字符长度，value为字符串
#     dic = dict((len(x),x) for x in ls)
#     return '最长的字符串为：%s ' % dic[max(dic)]
# print(func('123','adfadfs','gaoyan'))


'''3.定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档。
    例 print get_doc(urllib),则会输出urllib这个模块的帮助文档。'''

#ecoding = UTF-8
import os

def get_doc(module):
    doc = 'pydoc %s' % module
    f = os.popen(doc)
    return f.read()

print(get_doc('os'))

'''4.定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。'''
# def get_text(filePath):
#     try:
#         f = open(filePath,'r',-1,'UTF-8')
#         return f.read()
#         f.close()
#     except:
#         return "文件不存在"
#
# print(get_text('File/test2.txt'))

'''定义一个方法get_dir(folder),folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表。提示（可以了解python的glob模块）'''
# import glob
#
# def get_dir(folder):
#     path = folder+'\\';
#     return glob.glob(path+"*.*")
#
# print(get_dir('E:\\PythonProject\\FirstDemo'))









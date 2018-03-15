#!/usr/bin/env python
# -*- coding utf-8 -*-

def main():
    '''使用普通只读'''
    # with open('data.dat', mode='r', encoding='gbk') as f:
    #     data = f.read()
    #     print(data)

    '''使用字节方式只读'''
    # with open('data.dat', mode='rb') as f:
    #     data = f.read()
    #     print('二进制输出：',data)
    #     print(str(data, encoding='gbk')) # 从二进制再转为str

    '''读写指针'''
    # with open('data.dat', mode='r+', encoding='gbk') as f:
    #     print(f.tell())  # 获取指针位置
    #
    #     data = f.read()  # 执行read()时指针至结尾.
    #     print(data)
    #     f.writelines('股分有限公司') # 执行write()时指针至结尾.
    #
    #     f.seek(0)  # 设置指针位置
    #
    #     data = f.read()  # 执行read()时指针至结尾.
    #     print(data)
    #
    #     print(f.tell())  # 获取指针位置

    '''使用a+打开文件'''
    # with open('data.dat', mode='a+', encoding='utf-8') as f:
    #     data = f.read() # 文件一打开指针就到了文件结尾，此时读取不到任务东西
    #     print(data)

    '''flush()刷新内存'''
    # with open('data.dat','r+', encoding='utf-8') as f:
    #     f2.write('索宁紧锁着眉头..')
    #     # 在文件没有关闭前write的数据是在内存中。
    #     # f2.flush()  # 主动写入硬盘
    #     i = input(">>>")  # 如果没有使用flush(),此时打开文件是没有写入数据的

    '''truncate截取'''
    # with open('data.dat', 'r+', encoding='utf-8') as f:
    #     print(f.seek(6))
    #     f.truncate() # 从指针位置截取.
    #
    #     f.seek(0) # 设置指针位置
    #     data = f.read()
    #     print(data)

    '''for line in file 循环读取每一行'''
    # with open('data.dat', 'r+', encoding='utf-8') as f:
    #     for (index, line) in enumerate(f):
    #         print(index, line)

    '''同上'''
    # with open('data.dat', 'r+', encoding='utf-8') as f:
    #     for line in f.readlines():
    #         print(line)


    '''同时打开两个文件'''
    # with open('data.dat','r') as f1, open('data2.dat', 'r') as f2:
    #     data1 = f1.read()
    #     data2 = f2.read()
    #     print(data1)
    #     print("========================")
    #     print(data2)


if __name__ == '__main__':
    main()

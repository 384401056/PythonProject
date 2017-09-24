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
    with open('data.dat', mode='a+', encoding='utf-8') as f:
        data = f.read() # 文件一打开指针就到了文件结尾，此时读取不到任务东西
        print(data)




if __name__ == '__main__':
    main()

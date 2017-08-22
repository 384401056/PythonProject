# coding:utf-8
import csv

class Write_to_csv:
    ''' 将html数据解析后存为.csv文件 '''
    def __init__(self, path, fields):
        # 创建csv文件，并写入表头字段,打开方式用a+时，写入到csv中会存在一行间一行的问题。
        # 将打开的方法改为ab+，就不存在这个问题了.
        self.path = path
        with open(self.path, 'wb')as fo:
            csv_writer = csv.writer(fo)
            # self.file = csv.writer(open('conutries.csv','ab+'))
            if fields:
                self.fields = fields
                csv_writer.writerow(self.fields)


    def __call__(self, data):
        with open(self.path, 'ab+')as fo:
            csv_writer = csv.writer(fo)
            csv_writer.writerow(data)

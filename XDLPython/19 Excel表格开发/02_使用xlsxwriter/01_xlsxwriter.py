#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlsxwriter

workbook = xlsxwriter.Workbook(r'C:\Users\Administrator\Desktop\hello.xls') # 建立文件
worksheet = workbook.add_worksheet('employee') # 建立sheet， 可以work.add_worksheet('')来指定sheet名，但中文名会报UnicodeDecodeErro的错误
worksheet.write(10,10 , 'Hello world') # 向A1写入
workbook.close()
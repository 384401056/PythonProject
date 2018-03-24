#!/usr/bin/env python
# -*- coding: utf-8 -*-


import xlrd
import json
import os
from datetime import date,datetime


def main():
    row_list = []

    data = xlrd.open_workbook(r'files/001.xlsx')
    table = data.sheets()[7] # 获取第7张表的数据。
    col_count = table.ncols
    row_count = table.nrows

    for r in range(2, row_count):
        obj = {}
        for c in range(col_count):
            # print(table.cell(r,c).ctype) # ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
            if c == 2 or c == 3 or c == 4 or c == 5 or c == 6 or c == 7:
                # obj[table.col_values(c)[1]] = table.row_values(r)[c]
                obj[table.col_values(c)[1]] = table.cell(r, c).value
            else:
                # obj[table.col_values(c)[0]] = table.row_values(r)[c]
                # 如果此单元格为日期格式
                if table.cell(r, c).ctype == 3:
                    # 将xldata单元格类型转为日期数据。
                    dt = xlrd.xldate_as_tuple(table.cell_value(r, c), 0)
                    dt_str = date(*dt[:3]).strftime('%Y/%m/%d')  # 格式化日期数据
                    obj[table.col_values(c)[0]] = dt_str
                # 如果值为 #VALUE!则赋值为空。
                elif table.cell(r,c).ctype == 5:
                    obj[table.col_values(c)[0]] = ''
                else:
                    obj[table.col_values(c)[0]] = table.cell(r, c).value
        print(r, obj)
        row_list.append(obj)
    with open('data.txt', 'w+', encoding='utf-8') as f:
        f.write(json.dumps({'data':row_list}))
    # print(json.dumps(row_list))

if __name__ == '__main__':
    main()
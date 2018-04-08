#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pymongo import MongoClient
import random as r
import random
import json


def randomName():
    """生成随机人名"""
    a1 = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
          '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
          '熊', '纪', '舒', '屈', '项', '祝', '董', '梁', '金', '高']
    a2 = ['玉', '明', '', '芳', '军', '玲', '林', '少', '晓', '恩', '泽', '', '子', '中', '你', '说', '生', '国', '年', '和', '自', '以',
          '乾', '坤', ]
    a3 = ['芬', '桐', '玲', '', '国', '斌', '龙', '山', '强']
    for i in range(15):
        name = r.choice(a1) + r.choice(a2) + r.choice(a3)
    return name


def randomAge():
    """生成年龄"""
    return random.randint(20,60)


def randomAddr():
    """生成地址"""
    a1 = ['云南省', '浙江省', '湖南省', '广西省', '四川省']
    a2 = ['昆明市', '曲靖市', '玉溪市', '昭通市', '丽江市', '普洱市', '保山市', '临沧市', '楚雄州', '红河州', '迪庆州', '文山州', '西双版纳州', '大理州', '德宏州',
          '怒江州']
    a3 = []

    with open('addr.txt', 'r+', encoding='utf-8') as f:
        for (index, line) in enumerate(f):
            a3.append(line.replace("\n", ""))
    for i in range(108):
        address = r.choice(a1) + r.choice(a2) + r.choice(a3)
    return address


def main():
    client = MongoClient('192.168.1.102', 27017)
    db = client['mytest']
    collection = db['user']

    for i in range(20001):
        collection.insert({
            "name": randomName(),
            "age": randomAge(),
            "address": randomAddr()
        })


if __name__ == '__main__':
    main()

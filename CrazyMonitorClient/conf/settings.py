#!/usr/bin/env python
# -*- coding: utf-8 -*-
configs = {
    'HostID': 1,  # 本机在数据库中的id
    'Server': '10.88.20.21',
    'ServerPort': 8000,
    'urls': {
        'get_configs': ['api/client/config', 'get'],  # 获取配置信息的接口.
        'server_report': ['api/service/report/', 'post'],  # 上传数据的接口.
    },
    'RequestTimeout': 30,
    'ConfigUpdateInterval': 300,  # 更新客户端配置信息的间隔.
}

# 操作系统语言默认为英文
languarge = 'en'

cmd_lang = {
    'cn':'^平均时间',
    'en':'^Average',
}


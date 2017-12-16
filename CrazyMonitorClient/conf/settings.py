#!/usr/bin/env python
# -*- coding: utf-8 -*-


configs = {
    'HostID': 1,  # 本机在数据库中的id
    'Server': '127.0.0.1',
    'ServerPort': 8000,
    'urls': {
        'get_configs': ['api/client/config', 'get'],  # 获取配置信息的接口.
        'server_report': ['api/client/server/report', 'post'],  # 上传数据的接口.
    },
    'RequestTimeout': 30,
    'ConfigUpdateInterval': 30,  # 更新客户端配置信息的间隔.
}

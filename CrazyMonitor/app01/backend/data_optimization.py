#!/usr/bin/env python
# -*- coding: utf-8 -*-
from CrazyMonitor import settings


class DataStore(object):


    def __init__(self, client_id, service_name, data, reids_conn):
        """
        :param client_id:
        :param service_name:
        :param data:
        :param reids_conn:
        """
        self.client_id = client_id
        self.service_name = service_name
        self.data = data
        self.reids_conn = reids_conn

    def process_and_save(self):
        """将数据存入redis中"""
        settings


        pass








def main():
    pass


if __name__ == '__main__':
    main()
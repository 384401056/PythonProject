#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.client import ClientHandler
from conf import settings
import logging

log = logging.getLogger('crazyclient')

class command_handler(object):

    def __init__(self, sys_args):
        self.sys_args = sys_args
        # 如参数长度小于2
        if len(self.sys_args) < 3:
            print('command is not right!')
            self.help_msg()
        self.command_allowcator()


    def command_allowcator(self):
        """分捡用户输入的不同命令"""
        if (self.sys_args[2] in settings.cmd_lang):

            # 设置语言
            settings.languarge = self.sys_args[2]

            # 如果有输入的方法法名，就执行
            if hasattr(self, self.sys_args[1]):
                func = getattr(self,self.sys_args[1])
                return func()
            else:
                print('command does not exist!')
                self.help_msg()
        else:
            self.help_msg()

    def help_msg(self):
        valid_command = '''
        params[1]:
        start      start monitor client.
        stop       stop monitor client.
        params[2]:
        cn         Chinese
        en         English'''
        exit(valid_command) # 交互式shell


    def start(self):
        # print('Going to start the monitor client.')
        log.info('Going to start the monitor client.')
        Client = ClientHandler()
        Client.forever_run()



if __name__ == '__main__':
    pass

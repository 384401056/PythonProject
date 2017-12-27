#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os,django
from app01.backend.trigger_handler import TriggerHandler
from app01.backend import data_processing
from CrazyMonitor import settings

class ManagementUtility(object):

    def __init__(self, argv):
        self.argv = argv or sys.argv[:]
        self.prog_name = os.path.basename(self.argv[0])
        self.setting_exception = None
        self.registered_actions = {
            'start': self.start,
            'stop': self.stop,
            'trigger_watch': self.trigger_watch,
        }
        self.argv_check()

    def argv_check(self):
        """检查输入的参数"""
        if len(self.argv) <2 :
            self.main_help_text()
        if self.argv[1] not in self.registered_actions:
            self.main_help_text()
        else:
            self.registered_actions[sys.argv[1]]() # 执行命令行的输入的方法名：start, stop, trigger_wacth


    def start(self):
        reator = data_processing.DataHandler(settings)
        reator.looping()

    def stop(self):
        pass

    def trigger_watch(self):
        """
        开始监听触发器报警
        :return:
        """
        trigger_watch = TriggerHandler(settings)
        trigger_watch.start_watch()



    def main_help_text(self):
        print('supported commands as flow:')
        for k,v in self.registered_actions.items():
            print('   %s\t' % k)
        exit()


    def execute(self):
        pass

def execute_from_command_line(argv=None):
    utility = ManagementUtility(argv)
    utility.execute()

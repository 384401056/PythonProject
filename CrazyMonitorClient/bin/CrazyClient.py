#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.main import command_handler

if __name__ == '__main__':
    client = command_handler(sys.argv)

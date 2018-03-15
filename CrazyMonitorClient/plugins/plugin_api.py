#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plugins.Linux import cpu, memory, network

def get_linux_cpu():
    return cpu.monitor()

def get_linux_mem():
    return memory.monitor()

def get_linux_nic():
    return network.monitor()
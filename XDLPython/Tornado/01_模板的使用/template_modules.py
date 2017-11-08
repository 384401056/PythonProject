#!/usr/bin/env python
# -*- coding utf-8 -*-

from tornado.web import UIModule
from tornado import escape

class custom(UIModule):
    def render(self, *args, **kwargs):
        return '<div class="progress"><div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: '+str(args[0])+'%;">'+str(args[0])+'%</div></div>'



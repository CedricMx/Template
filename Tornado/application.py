# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 soovii
# Cedric, cedric_mx@163.com

import os

import tornado.web

# Local import
from url import url

# Settings can check http://tornado.readthedocs.io/en/latest/web.html#tornado.web.Application.settings
settings = dict(
    debug=True,
    template_path=os.path.join(os.path.dirname(__file__), 'templates'),
    static_path=os.path.join(os.path.dirname(__file__), 'statics'),
)

application = tornado.web.Application(
    handlers=url,
    **settings
)

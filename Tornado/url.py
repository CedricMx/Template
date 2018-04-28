# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 soovii
# Cedric, cedric_mx@163.com

''' the url structure of website '''

from handlers.index import IndexHandler

url = [
    (r'/', IndexHandler),
]

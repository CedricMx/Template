# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 soovii
# Cedric, cedric_mx@163.com

import pymysql


class Db(object):
    def Session(self):
        return pymysql.connect('localhost', 'root', 'hijarvis', 'cedric_db')

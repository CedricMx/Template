# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 soovii
# Cedric, cedric_mx@163.com

from db import Db


def select_table(table, column, condition, value):
    session = Db().Session()
    cur = session.cursor()

    sql = 'select ' + column + ' from ' + table + \
        ' where ' + condition + " = '" + value + "'"
    cur.execute(sql)
    lines = cur.fetchall()
    return lines

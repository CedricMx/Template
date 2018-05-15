# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright (c) 2018
# Cedric Tan, cedric_mx@163.com
'''
Use uuid package to get unique id
unid1(): 基于时间戳和计算机主机
unid3(): 基于命名空间和字符MD5
unid4(): 随机生成
unid5(): 基于命名空间和一个字符的SHA-1加密的UUID
'''
import uuid

name = 'test_name'
namespace = 'test_namespace'


print(uuid.uuid1())

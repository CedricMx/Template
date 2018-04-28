# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018
# Cedric Tan, cedric_mx@163.com

import os
import logging

'''
logging type Level from low to high:
DEBUG: 输出详细信息，一般只有在诊断问题时才会关注这些信息
INFO: 确认一切都按照预期的方式在进行工作
WARING:表明出现了一些意外情况，或暗示在不久的将来会出问题（例如：磁盘空间不足）。但目前软件仍然按预期的方式在工作
ERROR: 出现了更严重的问题，软件的部分功能已经无法正常工作
CRITICAL: 出现了更严重的问题，软件的部分功能已经无法正常工作
'''

def logging_function():
    filepath = os.path.dirname(__file__)
    logpath = os.path.join(filepath, 'Log', 'example.log')

    # Setting log format
    logging.basicConfig(
        filename=logpath,
        level=logging.DEBUG,   # 根据配置的级别决定哪些被写进log里
        # filemode='w',  # 覆盖之前记录, 记录不叠加
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    return logging

if __name__ == '__main__':
    log = logging_function()
    log.info('fuckkkkkkkkkkkkkkkkk')


# # Create logger
# logger = logging.getLogger('TestLog')
# # Setting logger level
# logger.setLevel(logging.DEBUG)
# # Create console handler and set level to debug
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# # create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',)
# # add formatter to ch
# ch.setFormatter(formatter)
# # add ch to logger
# logger.addHandler(ch)
#
# logger.debug('tests')

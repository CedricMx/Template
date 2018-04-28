# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018
# Cedric Tan, cedric_mx@163.com

import os
import threading
import logging

def get_logger():
    filepath = os.path.dirname(__file__)
    logpath = os.path.join(filepath, 'Log', 'example.log')

    # Setting log format
    logging.basicConfig(
        filename=logpath,
        level=logging.DEBUG,   # 根据配置的级别决定哪些被写进log里
        # filemode='w',  # 覆盖之前记录, 记录不叠加
        format='%(asctime)s %(threadName)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    return logging

# Define a function will used by thread
def doubler(number, logger):
    logger.debug('doubler function executing')
    result = number * 2
    logger.debug('doubler function ended with: {}'.format(
        result))

if __name__ == '__main__':
    logger = get_logger()
    thread_names = ['Mike', 'George', 'Wanda', 'Dingbat', 'Nina']
    for i in range(5):
        # Create Thread
        my_thread = threading.Thread(
            target=doubler, name=thread_names[i], args=(i,logger))
        # Start Thread
        my_thread.start()

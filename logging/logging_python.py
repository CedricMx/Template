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

class Logger:  
    def __init__(self, logName, logFile):  
        self._logger = logging.getLogger(logName)  
        self._logger.setLevel(logging.DEBUG)
  
        log_dir = "./Log"  
        if os.path.exists(log_dir) == False:  
            os.mkdir(log_dir)  
  
        log_filename = log_dir+'/'+logFile  
  
        fh = logging.FileHandler(log_filename)  
        # fh.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", '%Y-%m-%d %H:%M:%S') 
        
        ch.setFormatter(formatter)
        fh.setFormatter(formatter) 
        
        self._logger.addHandler(ch)
        self._logger.addHandler(fh)

    def debug(self, msg):  
        if self._logger is not None: 
         
            self._logger.debug(msg)
    
    def info(self, msg):  
        if self._logger is not None: 
            print('y')
            self._logger.info(msg)  

    def error(self, msg):  
        if self._logger is not None: 
         
            self._logger.error(msg) 


if __name__ == '__main__':
    a = Logger('test', 'test.log')
    # b = Logger('test01', 'test01.log')
    a.info('bbbbbbb')
    a.error('bbbbbbb')
    # b.info('bbbbbbbdaaaaab')



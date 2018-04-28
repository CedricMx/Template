# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 soovii
# Cedric, cedric_mx@163.com

''' Use yaml package to get value of .yaml file '''

import os
import yaml

dirname = os.path.dirname(__file__)
yaml_file = os.path.join(dirname, 'settings.yaml')

with open(yaml_file, 'r') as file:
	config = yaml.load(file)
settings = config['settings']

oauth2_email = settings['oauth2_email']
oauth2_password = settings['oauth2_password']
address = settings['address']
port = settings['port']

print(oauth2_email)
print(oauth2_password)
print(address)
print(port)

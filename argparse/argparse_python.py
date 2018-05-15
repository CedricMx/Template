# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright (c) 2018 soovii
# Cedric, cedric_mx@163.com

import argparse


parser = argparse.ArgumentParser(description='gpu means if u use it ')
parser.add_argument('--gpus', type=str, default = None)
parser.add_argument('--batch-size', type=int, default=32)
args = parser.parse_args()

print (args.gpus)
print (args.batch_size)
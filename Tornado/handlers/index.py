# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 soovii
# Cedric, cedric_mx@163.com

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

# Local import
import methods.readdb as mrd


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        user_infos = mrd.select_table('users', '*', 'username', username)

        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                self.write('Welcome' + username)
            else:
                self.write('password error')
        else:
            self.write('user not exists')

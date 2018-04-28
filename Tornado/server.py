# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 soovii
# Cedric, cedric_mx@163.com

import tornado.ioloop
import tornado.options
import tornado.httpserver

from application import application
from tornado.options import define, options

define('port', default=8000, help='run the given port', type=int)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)

    print('Development server is running at http://127.0.0.1:%s' % options.port)
    print('Quit the server with Control-C')

    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()

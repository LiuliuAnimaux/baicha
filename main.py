#!/usr/bin/env python
# coding=utf-8
__author__ = 'larkin'

import tornado.web
import tornado.ioloop
import handlers

PORT = 7000

if __name__ == "__main__":
    tornado.web.Application(handlers.HANDLERS).listen(PORT)
    tornado.ioloop.IOLoop.instance().start()

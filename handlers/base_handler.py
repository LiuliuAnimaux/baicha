#!/usr/bin/env python
# coding=utf-8

import tornado.web

class BaseHandlerOverrideMethod(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass


class BaseHandler(BaseHandlerOverrideMethod):
    def get(self, *args, **kwargs):
        self.finish('get base handler')

    def post(self, *args, **kwargs):
        self.finish('get base handler')

    def delete(self, *args, **kwargs):
        self.finish('get base handler')

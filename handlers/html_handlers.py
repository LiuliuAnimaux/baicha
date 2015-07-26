__author__ = 'larkin'

import base_handler


class HomeHandler(base_handler.BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../html/home.html')


class ChoiceHandler(base_handler.BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../html/choice.html')


class UploadHandler(base_handler.BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../html/upload.html')


class ResultHandler(base_handler.BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../html/result.html')


class RankHandler(base_handler.BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../html/rank.html')

HANDLERS = []

import base_handler
HANDLERS += [(r'/', base_handler.BaseHandler)]

import html_handlers
HANDLERS += [(r'/home', html_handlers.HomeHandler)]
HANDLERS += [(r'/choice', html_handlers.ChoiceHandler)]
HANDLERS += [(r'/upload', html_handlers.UploadHandler)]
HANDLERS += [(r'/result', html_handlers.ResultHandler)]
HANDLERS += [(r'/rank', html_handlers.RankHandler)]

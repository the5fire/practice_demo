#coding:utf-8

from handlers.index import MainHandler

import tornado.web

application = tornado.web.Application([
    (r"/", MainHandler),
])


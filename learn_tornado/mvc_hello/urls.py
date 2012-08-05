#coding:utf-8

from handlers.index import MainHandler

import tornado.web
import os
SETTINGS = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    xsrf_cookies=True,
    cookie_secret="11oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    autoescape=None,
)

application = tornado.web.Application([
    (r"/", MainHandler),
], **SETTINGS
)

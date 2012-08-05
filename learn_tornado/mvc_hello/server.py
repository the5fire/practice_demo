#coding:utf-8

import tornado.ioloop
from urls import application

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

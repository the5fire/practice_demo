#coding:utf-8

def hello():

    f = open('testdd.txt', 'r')
    content = f.read()
    f.close()
    print content

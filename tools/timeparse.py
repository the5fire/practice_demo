#coding:utf-8

__author__ = 'the5fire'

'''
    parse time
'''

import time

def time2stamp(timestr, format_type='%Y-%m-%d %H:%M:%S'):
    return time.mktime(time.strptime(timestr, format_type))

def stamp2time(stamp, format_type='%Y-%m-%d %H:%M:%S'):
    return time.strftime(format_type, time.localtime(stamp))


if __name__ == '__main__':
    stamp = time.time()
    nowtime = stamp2time(stamp)
    print stamp, '-->', nowtime
    print
    stamp = time2stamp(nowtime)
    print nowtime, '-->', stamp
    print 
    print stamp, '-->', stamp2time(stamp)


#coding=utf-8
'''
    author:huyang
    date:2012-7-10
    blog:http://www.the5fire.net
'''
import urllib
import time
import threading

from optparse import OptionParser   
from workermanager import WorkManager
from workermanager import Work

class Timer(threading.Thread):
    '''
        用来检查线程池中的任务数，据此退出线程
    '''
    def __init__(self, workmanager):
        super(Timer, self).__init__()
        self.workmanager = workmanager
        self.start()

    def run(self):
        while True:
            call_quit_flag = False
            try:
                #print 'there are %s jobs remain.' % str(self.workmanager.check_queue())
                if not call_quit_flag and self.workmanager.check_queue() < 1:
                    call_quit_flag = True
                    self.workmanager.quit_thread()

                if call_quit_flag and self.workmanager.check_thread() < 1:
                    print '==========Travel Over=============='
                    break
                time.sleep(3)
            except Exception,e:
                print 'an exception occur in timer:%s' % str(e)
                break

def main(confile, thread_num, debug):
    '''
        主函数，功能如下：
        1、读取配置文件中的数据
        2、将读取的数据传入检查函数，并将函数放入队列中
        3、启动队列
    '''
    workmanager = WorkManager(thread_num = thread_num)
    f = open(confile, 'r')
    for line in f.readlines():
        try:
            url, keyword, httpcode = tuple(line.split('|'))
            workmanager.add_job(check, url = url, keyword = keyword, httpcode = httpcode, debug = debug)
        except Exception,e:
            print 'an exception occur when read file:%s' % str(e)
            continue
    f.close()
    workmanager.start_thread_pool()
    timer = Timer(workmanager)

def check(options):
    '''
        判断url内容是否含有关键字，且状态码与指定相同
    '''
    url, keyword, httpcode = options.get('url'),options.get('keyword'),options.get('httpcode')
    if options.get('debug'):
        print 'check %s' % url
    req = urllib.urlopen(url)
    if req.getcode() != int(httpcode):
        print 'http status code error on url:%s,except code:%s, actually code is:%s' % (httpcode,url,req.getcode())
        return 
    content = req.read()
    if keyword not in content:
        print 'keyword error on url:%s,not found %s' % (url,keyword)


if __name__ == '__main__':
    usage = "usage: %prog  -c config.ini -t 100"

    parser = OptionParser(usage=usage)

    parser.add_option("-c", "--confile", dest="confile", default="config.ini",
                        help="local file path")

    parser.add_option("-t", "--thread_num", dest="thread_num", default = 1,
                        help="how many thread you want to run")

    parser.add_option("--debug", "--debug", dest="debug", default = False,
                        action="store_true",
                        help="show check info")

    (options, args) = parser.parse_args()
    import os
    #如果配置文件不存在，输入help信息
    if not os.path.isfile(options.confile):
        print 'the file:%s doesn\'t exist' % options.confile
        parser.print_help()
    
    main(options.confile, int(options.thread_num), options.debug)

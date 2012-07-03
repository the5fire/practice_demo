#coding=utf-8
'''
	author:the5fire
	blog:http://www.the5fire.net
	date:2012-07-03
'''

import time

def writefile(filename):
    counter = 0
    while True:
        writefile = open(filename, 'a')
        writefile.write('test' + str(counter) + '\n')
        counter += 1
        print  counter
        time.sleep(10)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        writefile(filename)

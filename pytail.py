#coding=utf-8
'''
	author:the5fire
	blog:http://www.the5fire.net
	date:2012-07-03
'''
import sys

last_num = 0

def get_last_line(filepath):
	'''
	获取未输入的行
	'''
	global last_num

	import  os
	if not os.path.exists(filepath):
		print 'no such file %s' % filepath
		sys.exit()
		return
	readfile = open(filepath, 'r')
	lines = readfile.readlines()
	if len(lines) > 20:
		last_num = 20	#首次输出最多输出20行
	if last_num < len(lines):
		print_lines = lines[last_num-len(lines):]
		for line in print_lines:
			print len(lines), last_num, line.replace('\n','')
		last_num = len(lines)
	readfile.close()



def timer(filename):
	'''
	每隔1秒执行一次
	'''
	while True:
		get_last_line(filename)
		import time
		time.sleep(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'illegal params'
    else:
        filename = sys.argv[1]
        timer(filename)

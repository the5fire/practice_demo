#coding=utf-8

import threading, Queue, time, sys

Qin = Queue.Queue()
Qout = Queue.Queue()
Qerr = Queue.Queue()
Pool = []

def report_error():
	Qerr.put(sys.exc_info()[:2])

def get_all_from_queue(Q):
	try:
		while True:
			yield Q.get_nowait()
	except Queue.Empty:
		raise StopIteration

def do_work_from_queue():
	while True:
		command, item = Qin.get()
		if command == 'stop':
			break
		try:
			if command == 'process':
				result = 'new' + item
			else:
				raise Value, 'Unknown command %r' % command
		except:
			report_error()
		else:
			Qout.put(result)

def make_and_start_thread_pool(number_of_threads_in_pool=5, daemons=True):
	for i in range(number_of_threads_in_pool):
		new_thread = threading.Thread(target=do_work_from_queue)
		new_thread.setDaemon(daemons)
		Pool.append(new_thread)
		new_thread.start()

def request_work(data, command='process'):
	Qin.put((command, data))

def get_result():
	return Qout.get()

def show_all_results():
	for result in get_all_from_queue(Qout):
		print 'Result:', result

def show_all_errors():
	for etyp, err in get_all_from_queue(Qerr):
		print 'Error:', etyp, err

def stop_and_free_thread_pool():
	for i in range(len(Pool)):
		request_work(None, 'stop')

	for existing_thread in Pool:
		existing_thread.join()
	
	del Pool[:]

if __name__ == '__main__':
	for i in ('_ba',7,'_bo'): request_work(i)

	make_and_start_thread_pool()
	stop_and_free_thread_pool()
	show_all_results()
	show_all_errors()

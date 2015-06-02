# -*- encoding: utf-8 -*-
'''
Created on 2015-04-23
Author: Aran
Description:
'''
from multiprocessing import Process
import os,time,random

def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

def func1():
    if __name__=='__main__':
        print 'Parent process %s.' % os.getpid()
        p = Process(target=run_proc, args=('test',))
        print 'Process will start.'
        p.start()
        p.join()
        print 'Process end.'

from multiprocessing import Pool,Queue
import os,time,random
def time_task(name):
    print 'Run task %s(%s)...' %(name,os.getpid())
    start = time.time()
    time.sleep(random.random()*10)
    end = time.time()
    print 'Task %s runs %0.2f seconds.'%(name,(end-start))
def func2():
    if __name__ == '__main__':
        print 'Parent process %s.' % os.getpid()
        p = Pool(4)
        for i in range(5):
            p.apply_async(time_task,args=(i,))
        print 'Waiting for all subprocesses done...'
        p.close()
        p.join()
        print 'All subprocesses done.'

def write(q):
    for value in ['A','B','C']:
        print 'Put %s to queue...' %value
        q.put(value)
        time.sleep(random.random())
def read(q):
    while True:
        value = q.get()
        print 'Get %s from queue.' % value

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))

    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
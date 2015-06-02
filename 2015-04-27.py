# -*- encoding: utf-8 -*-
'''
Created on 2015-04-27
Author: Aran
Description: review and thread
'''
# import os
# import  threading
# # print os.path.join(os.path.abspath('.'),'testdir','test.txt')
#
# print threading.current_thread().name
# def namePrint(ID):
#     print threading.current_thread().name , ID
# t = threading.Thread(target=namePrint, name = 'Threadtest',args=(1,))
# t.start()
# t.join()
#
# balance = 0
# lock = threading.Lock()
#
# def changeBalance(n):
#     global balance
#     balance =  n
#
# def run_thread(n):
#     lock.acquire()
#     try:
#         changeBalance(n)
#     finally:
#         lock.release()
#
# t1 = threading.Thread(target=run_thread,args=(100,))
# t2 = threading.Thread(target=run_thread,args=(20,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print balance

import threading

local = threading.local()

def process_print():
    print 'Hello, %s (in %s)' % (local.name, threading.current_thread().name)

def process_thread(name,):
    local.name = name
    process_print()

t1 = threading.Thread(target= process_thread, args=('Alice',))
t2 = threading.Thread(target= process_thread, args=('Bob',))

t1.start()
t2.start()
t1.join()
t2.join()
# print local

# import threading
#
# dict = {}
#
# def process_print():
#     print 'Hello, %s (in %s)' % (dict[threading.current_thread().name], threading.current_thread().name)
#
# def process_thread(name):
#     dict[threading.current_thread().name] = name
#     process_print()
#
# t1 = threading.Thread(target= process_thread, args=('Alice',))
# t2 = threading.Thread(target= process_thread, args=('Bob',))
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()


# import threading
#
# def process_print(name):
#     print 'Hello, %s (in %s)' % (name, threading.current_thread().name)
#
# def process_thread(name):
#     process_print(name)
#
# t1 = threading.Thread(target= process_thread, args=('Alice',))
# t2 = threading.Thread(target= process_thread, args=('Bob',))
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()
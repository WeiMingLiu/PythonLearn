# -*- encoding: utf-8 -*-
'''
Created on 2015-04-10
Author: Aran
Description:
'''

# from __future__ import division
import datetime
import functools
import sys
import module.test as test


try:
    import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import StringIO

def func2c1(func):
    def wrapper(*args):
        print 'execute %s()....' % func.__name__
        c =  func(*args)
        print 'finish %s()....' % func.__name__
        return c
    return wrapper

def func2cc1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            print '%s %s()...' %(text,func.__name__)
            func(*args)
        return wrapper
    return decorator

@func2cc1('call')
def func1(mood):
    print mood,
    print datetime.date.today()


@func2cc1('call')
def func2(name, score):
    print name, score

def func3():
    args = sys.argv
    print 'Hello, your argv is:',
    print args[1:]

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score


# func1('happy')
# func2('Aran', 99)
# print int('111',2)
# test.func()
# print sys.path
# print 10/3
aran = Student('test',90)
aran.name = 'aran'
print aran.name,aran.score
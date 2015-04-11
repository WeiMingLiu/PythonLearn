# -*- encoding: utf-8 -*-
'''
Created on 2015-4-9
@author: Aran
Description:
'''
def func1(*args):
    ans =0
    for n in args:
        ans = ans +n
    return ans

def func2(*args):
    def func2i1():
        ans = 0
        for n in args:
            ans = ans + n
        return ans
    return func2i1

def func3():
    print 'inFunc3'
    def func3i1():
        print 'InFunc3i1'
    func3i1()
    print 'outFunc3'

def func4():
    l=[]
    for i in range(0,100):
        def func4i1():
            l.append(i)
        func4i1()
    return l

#Tutorial

def count():
    fs = []
    for i in range(1,4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs

def build(x):
    return lambda: x


def func6(fun):
    def func6i1():
        print 'call %s()' % fun.__name__
        return fun()
    return func6i1

@func6
def func5():
    print 'executing func5'

# print func1(1,2,3,4,5,6,7,8,9)
# f = func2(1,2,3,4,5,6,7,8,9)
# func3()
# print func4()
# print [x() for x in count()]

# f = lambda x: x*x
# print f
# x = build(1)
# print x()


func5()
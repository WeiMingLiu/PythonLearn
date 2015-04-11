# -*- endcoding: utf-8 -*-
'''
Created on 2015-04-07
@author: Aran
Description:Mainly Review previous knowledge and Function new
'''
import sys
def func1():
    print "hello world"
    print "hello""world"
    print 'hello''world'
    print 'hello' + 'world'
    print "hello\nworld"
    print 'hello'
    print 'world'
    sys.stdout.write("hello\tworld\n")

def func2():
    name = raw_input("Please input your name:\n")
    print "Hi %s, your score is %d. \n" % (name, 99)


def func3():
    answer = input("Please input your Python expression:\n")
    sys.stdout.write('Hi, Answer is : ')
    print answer

def func4():
    print type(123)
    print type('Aran')
    print type(8.898)
    print type(2==5)
    print type(False)
    print type(None)

    print isinstance(123,int)
    print isinstance('Aran',str)
    print isinstance(2.898,float)
    print isinstance(2==5,bool)
    print isinstance(False,bool)

def func5():
    print ord('a')

def func6():
    list = ['a','b','c','d','e','f','g','h','i','j','k']

    print None,None,len(list),list
    print list.append('l'),len(list),list
    print list.insert(0,'aa'),len(list),list
    print list.pop(),list.pop(0),len(list),list

def func7():
    a= ['a1','a2'];
    b=('b1','b2');
    print a,b
    a[0]='aa'
    #b[0]='bb'  error
    print a,b
    a.pop()
    #b.pop()    error
    print a,b

def func8():
    dd = {'Mike':95, 'Bob':96, 'Jenny':92, 'Aran':99}
    dd['Tomas'] = 99
    print dd
    dd['Tomas'] = 98
    print dd
    print 'Aran' in dd
    print dd.get('Kim'), dd.get('Kim','NotExist')

def func9():
    ss= set(['Allen','Bob','Crystal','David','Eclipse'])
    ss.add('kk')
    ss.remove('Eclipse')
    print ss

def func10():
    b = ['b1','b2']
    ss= set(b)
    tt= (b,)
    b[0] = 'B1'
    b[1] = 'B2'
    print b,ss,tt

def func11(a,b):
    return a if a>b else b

def func12(x):
    for m in range(x):
        print m

def func13(x,y):
    return x,y


def func14(name, sex, age, job ='student', *args, **kwargs):
    return name,sex,age,job,args,kwargs

def func15():
    L = []
    n = 1
    while n <= 99:
        L.append(n)
        n = n +2
    return L

#slice
def func16(m,n):
    L =range(99)
    return L[m:n]

def func17(n):
    L = range(999)
    return L[::n]

#Iterable
def func18():
    dd = {'a':1,'b':2,'c':3,'d':4,'e':5}
    for kk in dd:
        print kk, dd[kk]
    for vv in dd.itervalues():
        print 'value: ',vv
    for kk,vv in dd.iteritems():
        print kk,vv

def func19():
    tt = ('b','a','c','e','g')
    for i in enumerate(tt):
        print i

def func20():
    print [x*x for x in range(1,11)]
    print [x*x for x in range(1,11) if x%2 == 0]
    print [s.lower() for s in ['Hello','World','IBM','Apple']]
    print [m+n for m in 'ABC' for n in 'XYZ']
    print [m+n+z for m in 'AB' for n in 'XY' for z in 'PQ']

#Generator
def func21():
    g = (x*x for x in range(1,4))
    print g
    print g.next(),g.next(),g.next()
    print g.next()
#func1()
#func2()
#func3()
#func4()
#func5()
#func6()
#func7()
#func8()
#func9()
#func10()
#print func11(1,2)
#func12(12)
#print func13(1,2)
#print func14('Aran','Male','23','studnet',*('java','C++'),**{'college':'USTC','major':'Software'})
#print func14('Aran','Male','23','student','java','C++',college='USTC',major='Software')
#print func15()
#print func16(5,11)
#print func17(5)
#func18()
#func19()
#func20()
func21()
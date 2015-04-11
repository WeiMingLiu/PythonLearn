# -*- encoding: utf-8 -*-
'''
Created on 2015-4-8
@author: Aran
Description:
'''

def func1():
    g = (m+n+z for m in 'ABC' for n in 'XYZ' for z in '123')
    print g.next()
    for n in g:
        print n

#Fibonacci
def func2(n):
    L = [1,1]
    if n == 0:
        print 1
    elif n == 1:
        print 1
    elif n>1:
        for i in range(1,n):
            L.append(L[-1]+L[-2])
        print L[n]
    print L[:]

#Fibonacci
def func3(max):
    n,a,b =0,0,1
    while n<max:
        print b
        a,b = b,a+b
        n = n+1

#Fibonacci Generator
def func4(max):
    n,a,b =0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n = n+1

#Yield for Generator
def func5():
    print 'Step 1'
    yield 1
    print 'Step 2'
    yield 2
    print 'Step 3'
    yield 3

#callback func
def func6(x, y, f):
    return f(x)+f(y)

#Map
def func7(x):
    return x*x +1

#reduce
def func8(x,y):
    return x*10+y

def func9(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

def func10(str):
    return reduce(func8,map(func9,str))

#Excerise Time：
def lowcapChange(str):
    return str[0].capitalize() + str[1:].lower()

def lowcapChanges(L):
    return map(lowcapChange, L)


def prod(x,y):
    return x*y

def func11(n):
    return n%2 == 0

#Excerise Time
def primeJudege(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        p = n/2
        for i in range(2,p+1):
            if n%i == 0:
                return False
        return True

def func12(d1,d2):
    if d1>d2:
        return 0
    else:
        return -1

def func13(s1,s2):
    ss1 = s1.lower();
    ss2 = s2.lower();
    if ss1<ss2:
        return -1
    else:
        return 1
#func1()
#func2(5)
#func3(5)
# print func5().next()
# print func5().next()
# print func5().next()
# g= func5()
# print g.next()
# print g.next()
# print g.next()
# print func6(-10,-20,abs)
# print map(func7,[1,2,3,4,5,6,7,8,9,10])
# print map(str,[11,22,33,44,55,66,77,88,99,100])
# print reduce(func8,[3,5,7,1,6,0,1,0])
# print func10('9231297'),type(func10('9231297'))

#Excerise Time:
# print lowcapChange('sdasd')
# print lowcapChanges(['adam', 'LISA', 'barT'])

# print reduce(prod,[2,4,8,32,5,32,0])

#print filter(func11,range(1,101))

# print filter(primeJudege,range(1,101))

# print sorted([36, 5, 12, 9, 21,34,12],func12)

print sorted(['bob', 'about', 'Zoo', 'Credit'], func13)
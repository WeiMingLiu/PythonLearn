# -*- encoding: utf-8 -*-
'''
Created on 2015-04-13
Author: Aran
Description:
'''
import types
from types import MethodType

class Cla1(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def cla1print(self):
        print self.__name, self.__score

    def gradeprint(self):
        if self.score >=90:
            print 'A'
        elif self.score >=60:
            print 'B'
        else:
            print 'C'


class Cla2(object):
    pass

def set_name(self,name):
    self.name = name

class Cla3(object):
    __slots__ = ('name','age')


class Cla4(object):

    def get_score(self):
        return self._score

    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        elif value <0 or value >100:
            raise ValueError('score must between 0 ~ 100!')
        else:
            self._score = value

class Cla5(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        elif value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        else:
            self._score = value

class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a+self.b
        if self.a > 1000000:
            raise StopIteration
        return self.a

    def __getitem__(self, n):
        if isinstance(n,int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            a,b = 1,1
            L =[]
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b,a+b
            return L

class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a
        if isinstance(n,slice):
            start = 0 if n.start == None else n.start
            stop = 100 if n.stop == None else n.stop
            a,b =1,1
            L=[]
            for x in range(stop):
                if x>= start:
                    L.append(a)
                a,b = b,a+b
            return L

# aran = Cla1('aran',69)
# aran.cla1print()
# aran.gradeprint()

# print hasattr('sdas','__len__')
# print 'sdasd'.__len__()
# print
# c = Cla2()
# c.name = 'Aran'
# print c.name

# Cla2.ssname = MethodType(set_name,None,Cla2)
# c = Cla2()
# c.ssname('Bom')
# print c.name
# print hasattr(c,'ssname')

# c = Cla3()
# c.name = 'Aran'
# c.age = 23
# c.score = '98'

# c = Cla4()
# c.set_score(99)

# c = Cla5()
# c.score = 2

# for n in Fib():
#     print n

print Fib()[0:8]
# print dir(slice.stop)
#print type(slice.stop)
# -*- encoding: utf-8 *-*
'''
Created on 2015-04-14
Author: Aran
Description:
'''
import logging
class Cla1(object):

    @property
    def score(self):
        return  self._score

    def __getattr__(self, item):
        if item == 'score':
            print 'if'
            return 100
        raise AttributeError("\'Cla1\' has no attribute: \'%s\'" %item)


class Cla2(object):
    def __init__(self,path=''):
        self._path = path
    def __getattr__(self, path):
        return Cla2('%s/%s' %(self._path,path))
    def _str_(self):
        return self._path

class Cla3(object):
    def __call__(self):
        print '__call__'


def func1(self,name):
    self._name = name
    print name

Cla4c = type('Cla4',(object,),dict(hello=func1))
h =Cla4c()
h.hello('aran')

class Cla4(object):
    hello = func1
Cla4c = Cla4
h = Cla4c()
h.hello('aran')

# try:
#     print 'try...'
#     r = 10/int('0')
#     print 'result:',r
# except ValueError,e:
#     print 'ValueError',e
# except ZeroDivisionError,e:
#     # print 'ZeroDivisionError:',e
#     logging.exception(e)
# else:
#     print 'no error!'
# finally:
#     print 'finally...'


# cla = Cla3
# dd =cla()
# dd()
# cc = Cla1()
# print getattr(cc,'score')

# print cc.score
#
# Cla2().ssda.xxc.wqwe.xc.sda
#
# dd = Cla3()
# dd()
#
# print callable(dd)
# print callable(cc)

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)

main()
print 'END'
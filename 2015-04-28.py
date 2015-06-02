# -*- encoding: utf-8 -*-
'''
Created on 2015-04-28
Author: Aran
Description:
'''

# print 'ABC\\-001'

import re

test = 'qq1041149156'
s = r'^[Q|q]{2}\d*'
re_s = re.compile(s)
if re_s.match(test):
    print True
else:
    print False


test = 'a b  c    d'
s = r'\s+'
print re.split(s,test)

test = '2312020000'
s = r'(^\d+?)(0*$)'
m = re.match(s,test)
print m.groups()

from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print p.x,p.y

from collections import deque
L = ['a','b','c']
q = deque(L)
q.append('y')
q.appendleft('x')
print q

from collections import Counter
c= Counter()
for ch in 'Programmer':
    c[ch] = c[ch] + 1
print c

import hashlib
md5 = hashlib.md5()
md5.update("My name is AranLiu.")
print md5.hexdigest()
# -*- encoding: utf-8 -*-
'''
Created on 2015-04-23
Author: Aran
Description:
'''

import os
import glob
import sys
import shutil
def func1():
    try:
        f = open('Stream.txt','r')
        print f.read()
    except IOError,e:
        pass
    finally:
        if f:
            f.close()

# func1()

def func2():
    with open('Stream.txt','rb') as f:
        print f.readline().strip()
        print f.readline()
# func2()

def func3():
    with open('Stream.txt','w') as f:
        f.write('Hello,world')
        f.write('Hello,world')

# func3()

def func4():
    f = open('Stream.txt','w')
    f.write('sss')
    f.close()
    f.write('dddd')

#excerise
def search(str,path=os.path.abspath('.')):
    for x in os.listdir(path):
        if os.path.isdir(x):
            search(str,os.path.join(path,x))
        else:
            if str in x:
                print os.path.join(path,x)



try:
    import CPickle as pickle
except ImportError:
    import pickle
# d = dict(name='Bob',age=20,score=88)
# dp = pickle.dumps(d)
# print dp
# d = pickle.loads(dp)
# print d
d = dict(name='Bob',age=20,score=88)
with open('dump.txt','wb') as f:
    pickle.dump(d,f)
with open('dump.txt','rb') as f:
    d = pickle.load(f)
print d
# func4()

import json
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
s = Student('Bob', 88)
#序列化
print(json.dumps(s.__dict__))
#反序列化
print(json.loads(json.dumps(s.__dict__),object_hook=lambda d:Student(d['name'],d['score'])))

# for file in os.listdir('.'):
#     print file

# for file in glob.glob('*.py'):
#     print file

# print os.path.join(os.path.abspath('.'),'testdir','test.txt')

# print [x for x in os.listdir('.') if os.path.isdir(x)]
#
# print [x for x in os.listdir('.') if os.path.splitext(x)[1]=='.py']

# print os.listdir(os.path.join('.','module'))

# search('2015')

print '我们的带三大'

func2()
# -*- encoding: utf-8 -*-
'''
Created on 2015-04-20
Author: Aran
Description:
'''
import logging
import pdb
logging.basicConfig(level = logging.INFO)
class Error1(StandardError):
    pass

def func1(s):
    n = int(s)
    if n==0:
        raise Error1('invalid value %s' %s)
    return 10/n


def func2(s):
    pdb.set_trace()
    # logging.info('n is zero')
    return s
func2(0)

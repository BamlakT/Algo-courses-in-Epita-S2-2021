# -*- coding: utf-8 -*-
"""
to compare execution durations...
"""

import time

# return the function result, duration is displayed
def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print(f.__name__, 'function took',(time2-time1)*1000.0,'ms')
        return ret
    return wrap

# return both the function result and the duration    
def timing_ret(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        t = (time2-time1)*1000.0
        print(f.__name__, 'function took', t ,'ms')
        return (ret, t)
    return wrap    
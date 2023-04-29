# -*- coding: utf-8 -*-
"""
to help testing functions on random lists
"""
from random import randint

def random_list(n, maxval):
    '''
    build a list with n random values in [0, maxval]
    '''
    L = []
    for i in range(n):
        L.append(randint(0, maxval))
    return L
    
def random_sorted_list(n, step):
    '''
    build a sorted list with n natural integers
    step is the maximum difference between values
    '''
    L = [0]
    for i in range(1, n):
        L.append(L[i-1] + randint(0, step))
    return L
    
    
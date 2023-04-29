# -*- coding: utf-8 -*-
"""
Lists: classical sorts
S1-S2
"""

from algopy import listtools
from algopy import timing

#------------------------------------------------------------------------------
    
"""
1.1 Selection sort
"""

def minimum(L, start, end):
    '''
    L: a non empty list
    start, end: 0 <= start < end < len(L)
    returns the position of the mimimum in L between 
    the positions start and end both included
    '''
    pos = start
    for i in range(start+1, end+1):
        if L[i] < L[pos]:
            pos = i
    return pos

def minimum2(L, start, end):
    '''
    L: a non empty list
    start, end: 0 <= start < end < len(L)
    returns the position of the mimimum in L between 
    the positions start and end both included
    '''
    while start < end:
        if L[start] < L[end]:
            end = end - 1
        else:
            start = start + 1
    return start
    
@timing.timing
def selectSort(L):
    '''
    L: list
    sorts the list L in place
    '''
    n = len(L)
    for i in range(n):
        pos = minimum(L, i, n-1)
        (L[i], L[pos]) = (L[pos], L[i]) # swap
        
'''
In one function, minimum inlined
'''

def selectSort2(L):
    '''
    L: list
    sorts the list L in place
    '''
    n = len(L)
    for i in range(n-1):
        minpos = i
        for j in range(i + 1, n):
            if L[j] < L[minpos]:
                minpos = j
        (L[i], L[minpos]) = (L[minpos], L[i])

#------------------------------------------------------------------------------

"""
1.2 Insertion sort
"""

def insert(x, L):
    '''
    x: element
    L: sorted list
    inserts x at its place in the sorted list L
    '''
    n = len(L)
    # search position
    i = 0
    while i < n and x > L[i]:
        i += 1
    # shifts
    L.append(None)
    for j in range(n, i, -1):
        L[j] = L[j-1]
    # insertion
    L[i] = x

def insert2(x, L):
    '''
    x: element
    L: sorted list
    inserts x at its place in the sorted list L
    the function searches the position and shifts at the same time
    '''
    i = len(L) - 1
    L.append(None)
    while i >= 0 and x < L[i]:
        L[i+1] = L[i]
        i -= 1
    L[i+1] = x

@timing.timing    
def insertSort(L):
    '''
    L: list
    sorts the list L not in place
    '''
    R = []
    for x in L:
        insert2(x, R)
    return R
    
'''
In place
'''

def __insert(x, L, n): 
    '''
    x: element
    L: sorted list
    n: 1 < n < len(L)
    inserts x at its position in the sorted list L[0, n[
    '''
    # search position
    i = 0
    while (i < n) and (x > L[i]):
        i += 1
    # shifts
    for j in range(n, i, -1):
        L[j] = L[j-1]
    # insertion
    L[i] = x

@timing.timing
def insertSort2(L):
    '''
    L: list
    sorts the list L in place
    '''
    for i in range(1, len(L)):
        __insert(L[i], L, i)

# in one function: insert2 inlined
def insertSort3(L):
    '''
    L: list
    sorts the list L in place
    '''
    for i in range(len(L)):
        x = L[i]
        j = i - 1
        while j >= 0 and x < L[j]:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = x
        
def binarySearch_iter(L, x):
    '''
    L: list
    x: element
    returns the index of element x in L if it is present
    the index where it should be otherwise
    '''
    left = 0
    right = len(L)
    while left < right:
        mid = left + (right - left) // 2
        if x == L[mid]:
            left = mid
            right = mid
        else:
            if x > L[mid]:
                left = mid + 1
            else:
                right = mid
    return right
    
def __binarySearch_rec(L, x, left, right):
    '''
    L, left, right: the list L[left, right[ is considered
    x: element
    returns the index of element x in L if it is present
    the index where it should be otherwise
    '''
    if left >= right:
        return right
    else:
        mid = left + (right - left) // 2
        if x == L[mid]:
            return mid
        else :
            if x > L[mid]:
                return __binarySearch_rec(L, x, mid+1, right)
            else:
                return __binarySearch_rec(L, x, left, mid)

def binarySearch_rec(L, x):
    '''
    L: list
    x: element
    returns the index of element x in L if it is present
    the index where it should be otherwise
    '''
    return __binarySearch_rec(L, x, 0, len(L))

#------------------------------------------------------------------------------
        
"""
1.3 Bubble sort
"""

@timing.timing
def bubbleSort(L):
    '''
    L: list
    sorts the list L in place
    '''
    swap = True
    n = len(L)
    while swap:
        swap = False
        for i in range(n-1):
            if L[i] > L[i+1]:
                (L[i], L[i+1]) = (L[i+1], L[i])
                swap = True
        n -= 1

@timing.timing
def bubble2(L):
    '''
    L: list
    sorts the list L in place
    '''
    n = len(L)
    change = 1
    while change != 0:
        change = 0
        for i in range(n-1):
            if L[i] < L[i+1]:
                 (L[i], L[i+1]) = (L[i+1], L[i])
                 change = i + 1
        n = change
            
#------------------------------------------------------------------------------
        
"""
2.1 Merge sort
"""

def partition(L):
    '''
    L: list
    splits L into two (new) lists of almost identical lengths
    and returns them
    '''
    n = len(L)
    L1 = []
    for i in range(0, n//2):
        L1.append(L[i])
    L2 = []      
    for i in range(n//2, n):
        L2.append(L[i])
    return (L1, L2)

def merge(L1, L2):
    '''
    L1: sorted list
    L2: sorted list
    merges two lists L1 and L2, sorted in increasing order,
    into one new sorted list.
    '''
    R = []
    i = 0
    j = 0
    n1 = len(L1)
    n2 = len(L2)
    while (i < n1) and (j < n2):
        if L1[i] <= L2[j]:
            R.append(L1[i])
            i = i+1
        else:
            R.append(L2[j])
            j = j+1
    for i in range(i, n1):
        R.append(L1[i])
    for j in range(j, n2):
        R.append(L2[j])
    return R

def merge2(L1, L2):
    '''
    L1: sorted list
    L2: sorted list
    merges two lists L1 and L2, sorted in increasing order,
    into one new sorted list.
    '''
    R = []
    n1 = len(L1)
    n2 = len(L2)
    (i1, i2) = (0, 0)
    for i in range(n1 + n2):
        if (i2 == n2) or (i1 < n1 and L1[i1] <= L2[i2]):
            R.append(L1[i1])
            i1 += 1
        else:
            R.append(L2[i2])
            i2 += 1         
    return R

def mergesort(L):
    '''
    L: list
    sorts the list L not in place
    '''
    if len(L) <= 1:
        return L
    else:
        (L1, L2) = partition(L)
        return merge(mergesort(L1), mergesort(L2))

@timing.timing
def callMergeSort(L):
    '''
    hat function for timing
    '''
    return mergesort(L)    
    
#------------------------------------------------------------------------------

"""
2.2 Bonus: Quick sort
"""

def __partition_p(L, left, right):
    '''
    L: list
    left, right: 0 <= left < right <= len(L)
    in L[left, right[ moves all values smaller than 
    mid point (pivot) in the left part 
    and higher value in the right part
    returns the new position of the pivot
    '''
    pivot = left + (right - left) // 2
    pval = L[pivot]
    (L[pivot], L[right-1]) = (L[right-1], L[pivot])
    pivot = left
    for i in range(left, right-1):
        if L[i] <= pval:
            (L[pivot], L[i]) = (L[i], L[pivot])
            pivot += 1
    (L[pivot], L[right-1]) = (L[right-1], L[pivot])
    return pivot

def __qsort(L, left, right):
    '''
    L: list
    left, right: 0 <= left <= right <= len(L)
    sorts in place the sublist L[left, right[ (between positions left included and right not included)
    '''
    if right - left > 1:
        pivot = __partition_p(L, left, right)
        __qsort(L, left, pivot)
        __qsort(L, pivot + 1, right)

@timing.timing
def quickSort(L):
    '''
    L: list
    sorts the list L in place
    '''
    __qsort(L, 0, len(L))

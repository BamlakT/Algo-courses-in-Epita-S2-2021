#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Undergraduate Epita - S2
Binary Trees: tests
'''

from algopy import bintree, queue

#-------------------------------------------------------------------------------

''' 
test degenerate
'''

# not the most optimized (too many tests)
def degenerate0(T):
    '''
    T: bintree
    returns True if T is degenerate, False otherwise
    '''
    if T == None:
        return True
    elif T.left != None and T.right != None:
        return False 
    else:
        return degenerate0(T.left) and degenerate0(T.right)


# None case in call function + each node case: too many tests again 
def __degenerate00(T):
    '''
    T: bintree
    returns True if T is degenerate, False otherwise
    '''
    if T.left != None and T.right != None:
        return False 
    else:
        if T.left == None and T.right == None:
            return True
        else:
            if T.left != None:
                return __degenerate0(T.left) 
            else:
                return __degenerate0(T.right)

def degenerate00(T):
    '''
    T: bintree
    returns True if T is degenerate, False otherwise
    '''
    return T == None or __degenerate00(T)


# the optimized version (only 2 tests each time): separate the tests on empty subtrees     
def __degenerate(B):
    '''
    B: not empty bintree
    returns True if B is degenerate, False otherwise
    '''
    if B.left == None:
        if B.right == None:
            return True
        else:
            return __degenerate(B.right)
    else:
        if B.right == None:
            return __degenerate(B.left)
        else:
            return False
            
def degenerate(B):
    '''
    B: bintree
    returns True if B is degenerate, False otherwise
    '''
    return B == None or __degenerate(B)

# a nice version
def __degenerate2(B):
    '''
    B: bintree
    returns True if B is degenerate, False otherwise
    '''
    leftEmpty = (B.left == None)
    if B.right == None:
        return leftEmpty or __degenerate2(B.left)
    else:
        return leftEmpty and __degenerate2(B.right)
        
def degenerate2(B):
    '''
    B: bintree
    returns True if B is degenerate, False otherwise
    '''
    return B == None or __degenerate2(B)

#-------------------------------------------------------------------------------

''' 
test perfect (= complet !)
'''

# def1 : all leaves at same level + no single points => DFS

def __leftlength(B):
    '''
    B: bintree
    returns the length of the left branch starting from B
    '''
    h = 0
    T = B
    while T != None:
        h += 1
        T = T.left
    return h
    
def __perfect(B, h):
    '''
    B: non empty bintree
    h: the expected height
    returns True if B is perfect, False otherwise
    '''
    if B.left == None:
        if B.right == None:
            return h == 0   # leaf
        else:
            return False
    else:
        if B.right == None:
            return False
        else:
            return __perfect(B.left, h-1) and __perfect(B.right, h-1)
        
def perfect(B):
    '''
    B: bintree
    returns True if B is perfect, False otherwise
    '''
    if B == None:
        return True
    else:
        return __perfect(B, __leftlength(B.left))    


# version that computes the height going up

def __perfectup(B):
    '''
    B: non empty bintree
    returns (res, h):
    - res is True if B is perfect, False otherwise
    - h is the height of the current bintree B
    '''
    if B.left == B.right:
        return (True, 0)
    else:
        if B.left == None or B.right == None:
            return (False, -42)
        else:
            (okLeft, hLeft) = __perfectup(B.left)
            if not okLeft:
                return (False, -42)
            else:
                (okRigh, hRight) = __perfectup(B.right)
                return (okRigh and hLeft == hRight, hLeft + 1)

def isperfect_up(B):
    '''
    B: bintree
    returns True if B is perfect, False otherwise
    '''
    if B == None:
        return True
    else:
        (ok, _) = __perfectup(B)
        return ok

# def2: Each level has twice as many nodes as the previous one => BFS

def perfectWidth(B):
    '''
    B: bintree
    returns True if B is perfect, False otherwise
    '''
    if B == None:
        return True
    else:
        q = queue.Queue()
        q.enqueue(B)
        q.enqueue(None)
        (w, next_w) = (0, 1)
        perfect = True
        while not q.isempty() and perfect:
            T = q.dequeue()
            if T == None:
                if w != next_w:
                    perfect = False
                if not q.isempty():
                    next_w = w * 2
                    w = 0
                    q.enqueue(None)
            else:
                w = w + 1
                if T.left != None:
                    q.enqueue(T.left)
                if T.right != None:
                    q.enqueue(T.right)
        return perfect

#-------------------------------------------------------------------------------

''' 
test complete (= parfait !)
'''

def completeWidth(B):
    '''
    B: bintree
    returns True if B is complete, False otherwise
    '''
    if B == None:
        return True
    else:
        q = queue.Queue()
        q.enqueue(B)
        complete = True
        empty_child = False
        while not q.isempty() and not empty_child:
            T = q.dequeue()
            if T.left == None:
                empty_child = True
                complete = T.right == None
            else:
                q.enqueue(T.left)
                if T.right != None:
                    q.enqueue(T.right)
                else:
                    empty_child = True
        
        while not q.isempty() and complete:
            T = q.dequeue()
            complete = (T.left == None and T.right == None)
        return complete
   

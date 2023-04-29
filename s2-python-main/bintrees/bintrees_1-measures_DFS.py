#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Undergraduate Epita - S2
Binary Trees: measures and DFS
'''

from algopy import bintree

#-------------------------------------------------------------------------------
#1.1

def size(B):
    '''
    B: bintree
    returns the size of the bintree B
    '''
    if B == None:
        return 0
    else:
        return 1 + size(B.left) + size(B.right)

#-------------------------------------------------------------------------------
#1.2

def height(B):
    '''
    B: bintree
    returns the height of the bintree B
    '''
    if B == None:
        return -1
    else:
        return 1 + max(height(B.left), height(B.right))


#-------------------------------------------------------------------------------
#1.3

'''
DFS: Depth-First Search
'''

def dfs(B):
    if B == None:
        # terminal case
        pass
    else:
        # preorder
        dfs(B.left)
        # inorder
        dfs(B.right)
        # postorder
        
        
def __myprint(x):
    '''
    prints element x without endline
    '''
    print(x, sep='', end='')
  
  
def dfs_displayAA(B):
    '''
    B: bintree
    displays the Algebraic Abstract Type representation of the bintree B
    '''
    if B == None:
        __myprint('_')
    else:
        __myprint('<' + str(B.key) + ',')     
        # + is the concatenation operator on sequences
        dfs_displayAA(B.left)
        __myprint(',')
        dfs_displayAA(B.right)
        __myprint('>')
        
#-------------------------------------------------------------------------------
#1.4

'''
Serialization
<r, G, D> is "(rGD)"
'''

def to_linear(B):
    '''
    B: bintree
    returns the linear representation of the bintree B
    '''
    if B == None:
        return "()"
    else:
        s = '('
        s = s + str(B.key)
        s = s + to_linear(B.left)
        s = s + to_linear(B.right)
        s = s + ')'
    return s 

def to_linear2(B):
    '''
    B: bintree
    returns the linear representation of the bintree B
    '''
    if B == None:
        return "()"
    else:
        return '(' + str(B.key) + to_linear2(B.left) + to_linear2(B.right) + ')'
        
#-------------------------------------------------------------------------------
#1.5

def __pm(B, d): # or d=0
    '''
    B: bintree
    returns a pair (s, n):
    - s is the the path length
    - n is the number of nodes
    '''
    if B == None:
        return (0,0)
    else:
        nleft, sleft = __pm(B.left, d + 1)
        nright, sright = __pm(B.right d + 1)
        return (d + sleft + sright, 1 + nleft + nright)

def pm(B):
    '''
    B: bintree
    returns the average depth of the bintree B
    '''
    s, n = __pm(B, 0)
    if n == 0:
        return 0
    else:
        return s/n
        
def __pme(B, d): # or d=0
    '''
    B: bintree
    returns a pair (s, n):
    - s is the the external path length
    - n is the number of external nodes
    '''
    if B.left == None:
        if B.right == None:
            return (d, 1)
        else:
            return __pme(B.right, d + 1)
    else:
        if B.right == None:
            return __pme(B.left, d + 1)
        else:
            nleft, sleft = __pme(B.left, d + 1)
            nright, sright = __pme(B.right, d + 1)
            return (sleft + sright, nleft + nright)

def pme(B):
    '''
    B: bintree
    returns the external average depth of the bintree B
    '''
    s, n = __pme(B, 0)
    if n == 0:
        return 0
    else:
        return s/n

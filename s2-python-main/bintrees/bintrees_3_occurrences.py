#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Undergraduate Epita S2
Binary Trees: occurrences + hierarchical implementation
'''

from algopy import bintree, queue

#------------------------------------------------------------------------------
#3.2

# from BinTree to hierarchical representation

# version1: the size of the tree is given (n) 
#        -> the vector has the maximum length :(

def __bintree2hier(B, T, i=1):
    '''
    B: bintree
    T: vector containing the hierarchical representation of B
    i: index corresponding to the bintree B in T
    fills the vector T with the hierarchical representation of B
    '''
    if B != None:
        T[i] = B.key
        __bintree2hier(B.left, T, 2*i)
        __bintree2hier(B.right, T, 2*i+1)


def bintree_to_hier(B, n):
    '''
    B: bintree
    n: size of the bintree B
    builds and returns the hierarchical representation of B
    '''
    maxno = 2 ** n - 1
    H = []
    for _ in range(maxno + 1):
        H.append(None)
    __bintree2hier(B, H)
    return H

# version 2: the higher hierarchical number is computed by a first traversal 
#          = the size of the vector

def __get_size(B, i=1):
    '''
    B: bintree
    n: size of the bintree B
    returns the value of the greatest index needed to represent B
    '''
    if B == None:
        return 0
    else:
        no_left = __get_size(B.left, 2*i)
        no_right = __get_size(B.right, 2*i+1)
        return max(i, no_left, no_right)

def bintree_to_hier2(B):
    '''
    B: bintree
    builds and returns the hierarchical representation of B
    '''
    maxno = __get_size(B)
    H = []
    for _ in range(maxno + 1):
        H.append(None)
    __bintree2hier(B, H)
    return H

# version 3 (Bonus): the list grows when needed (vector size is the highest "hierarchical number")

def __extend_list(L, i):
    '''
    L: list
    i: index
    extends the size of the list L to size (i+1)
    '''
    for _ in range(len(L), i+1):
        L.append(None)
        
def __bintree_to_hier3(B, H, i = 1):
    '''
    B: bintree
    H: vector containing the hierarchical representation of B
    i: index corresponding to the bintree B in H
    fills the vector H with the hierarchical representation of B
    '''
    if B !=  None:
        __extend_list(H, i)
        H[i] = B.key
        __bintree_to_hier3(B.left, H, 2 * i)
        __bintree_to_hier3(B.right, H, 2 * i + 1)
    
def bintree_to_hier3(B):
    '''
    B: bintree
    builds and returns the hierarchical representation of B
    '''
    H = [None]
    __bintree_to_hier3(B, H)
    return H


#------------------------------------------------------------------------------
#3.3
# Occurrences

#Q1
# tree in the subject
# s1 = "{ε, 0, 1, 00, 10, 11, 000, 001, 111, 0010, 0011}"

#Q2
def occurrences_list(B):
    '''
    B: bintree
    returns the list of occurrences (str) of B's nodes
    note: 'ε' is char(949)
    result example: ['ε', '0', '1', '00', '10', '11', '000', '001', '111', '0010', '0011']
    '''
    L = []
    if B != None:
        q = queue.Queue()
        q.enqueue((B, ""))  # the queue contains (B: BinTree, occ: str the occurrence of B's root)
        while not q.isempty():
            (B, occ) = q.dequeue()
            L.append(occ) 
            if B.left != None:
                q.enqueue((B.left, occ + '0'))
            if B.right != None:
                q.enqueue((B.right, occ + '1'))
        L[0] = chr(949)    # replace "" by 'ε'
    return L
 
#------------------------------------------------------------------------------
#3.4
# prefix code

#Q3
B_codes = bintree.BinTree(' ', 
            bintree.BinTree('a', None, None),
            bintree.BinTree(' ', 
                    bintree.BinTree(' ', 
                            bintree.BinTree('u', None, None), 
                            bintree.BinTree('n', None, None)
                            ), 
                    bintree.BinTree(' ', 
                            bintree.BinTree(' ', 
                                    bintree.BinTree('f', None, None),
                                    bintree.BinTree('m', None, None)),
                            bintree.BinTree('H', None, None)
                            )
                    )
            )

#Q4

# occ is built going down
def __searchOcc(B, c, occ=""):
    '''
    B: non empty FULL tree
    c: letter
    occ: the occurence of the root
    '''
    if B.left == None:  # full => B.right == None
        if B.key == c:
            return occ
        else:
            return None
    else:
        res = __searchOcc(B.left, c, occ+'0')
        if res != None:
            return res
        else:
            return __searchOcc(B.right, c, occ+'1')
            
def __searchOcc2(B, c):
    '''
    B: non empty FULL tree
    c: letter
    occ: the occurence of the root
    '''
    if B.left == None:
        if B.key == c:
            return ""
        else:
            return None
    else:
        res = __searchOcc2(B.left, c)
        if res != None:
            return '0' + res
        else:
            res = __searchOcc2(B.right, c)
            if res != None:
                return '1' + res
            else:
                return None

def searchOcc(B, c):
    '''
    B: FULL tree
    c: letter
    returns the code of the given letter c
    '''
    if B == None:
        return None
    else:
        return __searchOcc(B, c) #__searchOcc2(B, c)

#------------------------------------------------------------------------------

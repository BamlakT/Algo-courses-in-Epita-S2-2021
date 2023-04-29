#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
S2
BST
'''

from algopy import bintree

#------------------------------------------------------------------------------

# BST -> list: DFS, add keys inorder
def __bst2list(B, L):
    '''
    B: BST
    L: list
    puts the keys of the BST B into the list L so that L is sorted
    '''
    if B != None:
        __bst2list(B.left, L)
        L.append(B.key)
        __bst2list(B.right, L)
        
def bst2list(B):
    '''
    B: BST
    builds and returns a sorted list with the element of the BST B
    '''
    L = []
    __bst2list(B, L)
    return L
    
#------------------------------------------------------------------------------

# list -> BST: warning, works only with strictly increasing lists!
# ~like a binary search ('dichotomie')
#  we work on [left, right[ here!

def __list2bst(L, left, right):
    '''
    L: strictly sorted list
    left, right: 0 <= left <= right <= len(L)
    returns a balanced BST using the sorted list L[left, right[
    '''
    if left == right:
        return None
    else:
        mid = left + (right-left) // 2
        B = bintree.BinTree(L[mid], None, None)
        B.left = __list2bst(L, left, mid)
        B.right = __list2bst(L, mid+1, right)
        return B
       
def list2bst(L):
    '''
    L: strictly sorted list
    returns a balanced BST using the sorted list L
    '''
    return __list2bst(L, 0, len(L))
    
#------------------------------------------------------------------------------

def __testbst(B, inf, sup):
    '''
    B: bintree
    inf, sup: bounds for B
    returns True if B is a BST with values in ]inf, sup], False otherwise
    '''
    if B == None:
        return True
    else:
        if B.key > inf and B.key <= sup:
            return __testbst(B.left, inf, B.key) \
                    and __testbst(B.right, B.key, sup)
        else:
            return False
        

def testbst(B):
    '''
    B: bintree
    returns True if B is a BST, False otherwise
    '''
    return __testbst(B, -float('inf'), float('inf'))


#------------------------------------------------------------------------------
# CLASSICS

# Researches

def minBST(B):
    '''
    B: non-empty BST
    returns the minimum value of B
    '''
    if B.left == None:
        return B.key
    else:
        return minBST(B.left)
    
def maxBST(B):
    '''
    B: non-empty BST
    returns the maximum value of B
    '''
    while B.right != None:
        B = B.right
    return B.key
    
#------------------------------------------------------------------------------

def searchBST(B, x):
    '''
    B: BST
    x: element
    returns the tree whose root contains x if x is in the BST B
    None otherwise
    '''
    if B == None:
        return None
    else:
        if x == B.key:
            return B
        else:
            if x < B.key:
                return searchBST(B.left, x)
            else: # x > B.key
                return searchBST(B.right, x)

def searchBST2(B, x):
    '''
    B: BST
    x: element
    returns the tree whose root contains x if x is in the BST B
    None otherwise
    '''
    if B == None or x == B.key:
        return B
    else:
        if x < B.key:
            return searchBST2(B.left, x)
        else: # x > B.key
            return searchBST2(B.right, x)
                        

def searchBST_iter(B, x):    
    '''
    B: BST
    x: element
    returns the tree whose root contains x if x is in the BST B
    None otherwise
    '''
    while B != None and x != B.key:
        if x < B.key:
            B = B.left
        else:
            B = B.right
    return B

#------------------------------------------------------------------------------

'''
insert(emptytree,x)= <x,emptytree,emptytree>
x≤r ⇒ insert(<r,L,R>,x) = <r, insert(L,x), R>
x>r⇒insert(<r,L,R>,x)=<r,L,insert(R,x)>
'''

def leaf_insert(B, x):
    '''
    B: BST
    x: element
    inserts the element x in the BST B at the leaf
    and returns the new root of the BST B after insertion
    '''
    if B == None:
        return bintree.BinTree(x, None, None)
    else:
        if x <= B.key:
            B.left = leaf_insert(B.left, x)
        else:
            B.right = leaf_insert(B.right, x)
        return B


def insert_iter(B, x):
    '''
    B: BST
    x: element
    inserts the element x in the BST B at the leaf
    and returns the new root of the BST B after insertion
    '''
    new = bintree.BinTree(x, None, None)
    if B == None:
        return new
    else:
        T = B
        while T != None:
            parent = T
            if x <= T.key:
                T = T.left
            else:
                T = T.right
        if x <= parent.key:
            parent.left = new
        else:
            parent.right = new
        return B

#------------------------------------------------------------------------------

# returns the resulting tree from the deletion!

def delete(B, x):
    '''
    B: BST
    x: element
    inserts the element x in the BST B if it is present
    and returns the new root of the BST B after deletion
    '''
    if B == None:
        return None
    else:
        if x == B.key:
#            if B.left == None and B.right == None:  # feuille
#                return None
            if B.right == None:   # single left point or leaf
                return B.left
            elif B.left == None:  # single right point
                return B.right
            else:   #double point
                B.key = maxBST(B.left)
                B.left = delete(B.left, B.key)
                return B
        else:
            if x < B.key:
                B.left = delete(B.left, x)
                
            else: # x > B.key
                B.right = delete(B.right, x)
                
            return B
            
#------------------------------------------------------------------------------

# Optimization

def del_max_bst(B):
    '''
    B: non-empty BST
    deletes the maximum value of B
    returns (B,m) where:
    - B is the new tree 
    - m is the deleted value
    '''
    if B.right == None:
        return (B.left, B.key)
    else:
        (B.right, m) = del_max_bst(B.right)
        return (B, m)


def del_bst_opti(B, x):
    '''
    B: BST
    x: element
    inserts the element x in the BST B if it is present
    and returns the new root of the BST B after deletion
    '''
    if B == None:
        return None
    else:
        if x == B.key:
            if B.left == None:
                return B.right
            elif B.right == None:
                return B.left
            else:
                (B.left, B.key) = del_max_bst(B.left)
                return B
        else:
            if x < B.key:
                B.left = del_bst_opti(B.left, x)
            else:
                B.right = del_bst_opti(B.right, x)
            return B

#------------------------------------------------------------------------------

#root insertion

def cut(B, x):
    '''
    B: BST
    x: root element
    cuts the BST B with the value x
    '''
    if B == None:
        return (None, None)
    else:
        if B.key <= x:
            L = B
            (L.right , R) = cut(B.right, x)
        else:
            R = B
            (L, R.left) = cut(B.left, x)
        return (L, R)

def root_insertion(B, x):
    '''
    B: BST
    x: element
    inserts the element x in the BST B as a new root
    '''
    (L, R) = cut(B, x)
    return bintree.BinTree(x, L, R)
    
#------------------------------------------------------------------------------

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Undergraduate Epita - S2
Binary Trees: tests
'''

from algopy import bintree

#-------------------------------------------------------------------------------

"""
Structure algo de création d'arbre

def build(....):
    if ???:
        return None
    else:
        B = bintree.BinTree(key, None, None)   
        B.left = build(???)
        B.right = build(???)
        return B
        
ou
        return bintree.BinTree(key, build(...), build(....))        
"""

#-------------------------------------------------------------------------------
#5.1

class BinTreeParent:
    def __init__(self, key, parent, left, right):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        
# first version: parent is passed as a parameter
def __copy(B, p):
    '''
    B: bintree (BinTree)
    p: parent of B
    returns the BinTreeParent version of B
    '''
    if B == None:
        return None
    else:
        C = BinTreeParent(B.key, p, None, None)
        C.left = __copy(B.left, C)
        C.right = __copy(B.right, C)
        return C

def copywithparent(B):
    '''
    B: bintree (BinTree)
    returns the BinTreeParent version of B
    '''
    return __copy(B, None)
    
# second version: parent is set going up
def __copy2(B):
    '''
    B: bintree (BinTree)
    returns the BinTreeParent version of B
    '''
    C = BinTreeParent(B.key, None, None, None)
    if B.left != None:
        C.left = __copy2(B.left)
        C.left.parent = C
    if B.right != None:
        C.right = __copy2(B.right)
        C.right.parent = C
    return C

def copywithparent2(B):
    '''
    B: bintree (BinTree)
    returns the BinTreeParent version of B
    '''
    if B == None:
        return None
    else:
        return __copy2(B)

#-------------------------------------------------------------------------------
#5.2

def hier_to_bintree(H, i=1):
    '''
    H: vector representing a bintree in hierarchical representation
    i: current position in the vector H
    builds and returns the BinTree version of H
    '''
    if i >= len(H) or H[i] == None:
        return None
    else:
        B = bintree.BinTree(H[i], None, None)
        B.left = hier_to_bintree(H, 2*i)
        B.right = hier_to_bintree(H, 2*i+1)
        return B
        
#-------------------------------------------------------------------------------
#5.3

def _from_linear(s, pos):
    '''
    s: string representing a binary tree
    pos: current position in the string s
    returns (tree, pos):
    - tree: BinTree version of s
    - pos: new position in the string s
    '''
    pos += 1    # pass the '('
    # Check for empty tree
    if s[pos] == ')':
        return (None, pos + 1)
    else:
        # Get BinTree key and create node
        key = ""
        while s[pos] != "(":
            key += s[pos]
            pos += 1
    
        tree = bintree.BinTree(int(key), None, None)
        # Parse children
        (tree.left, pos) = _from_linear(s, pos)
        (tree.right, pos) = _from_linear(s, pos)
        
        pos += 1 # pass the ')'
        return (tree, pos)


def from_linear_rep(s):
    '''
    s: string representing a binary tree
    builds and returns the BinTree version of s
    '''
    (T, _) = (s, 0)
    return T

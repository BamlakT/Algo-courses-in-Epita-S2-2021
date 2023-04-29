# -*- coding: utf-8 -*-
'''
AVL
'''
from algopy import bintree

#------------------------------------------------------------------------------
# test height-balanced

def __hbal(B):
    '''
    B: BinTree
    returns (b, h) where
    - b is True if B is height-balanced
    - h is the height of B
    '''
    if B == None:
        return (True, -1)
    else:
        (ok_left, h_left) = __hbal(B.left)
        if not ok_left:
            return (False, 38)
        else:            
            (ok_right, h_right) = __hbal(B.right)
            if abs(h_left - h_right) > 1:
                return (False, 42)
            else:
                return (ok_right, 1 + max(h_left, h_right))

def height_balanced(B):
    '''
    B: BinTree
    returns True if B is height-balanced, False otherwise
    '''
    (ok, h) = __hbal(B)
    return ok
    
#------------------------------------------------------------------------------
    
# trees for tests

B =  bintree.load("files/bst_hbalanced.bintree")
B1 = bintree.load("files/bst_not-hbalanced1.bintree")    # not a BST
B2 = bintree.load("files/bst_not-hbalanced2.bintree")    # not height-balanced
B3 = bintree.load("files/bst_wrong.bintree")             # not height-balanced

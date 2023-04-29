#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Undergraduate Epita - S2
Binary Trees: BFS
'''

from algopy import bintree, queue

#-------------------------------------------------------------------------------
#2.1

'''
BFS: Breadth-First Search (Level order traversal)
'''

def BFS(B):
    '''
    B: bintree
    prints the keys of the bintree B in hierarchical order
    '''
    if B != None:
        q = queue.Queue()
        q.enqueue(B)
        while not q.isempty():
            B = q.dequeue()
            print(B.key, end= ' ')
            if B.left != None:
                q.enqueue(B.left)
            if B.right != None:
                q.enqueue(B.right)
        
#-------------------------------------------------------------------------------
#2.2

def get_average(B):
    '''
    B: bintree
    builds and returns the list L:
    - len(L) = number of levels of the binary tree
    - L[i] = average of the key values at level i
    '''
    if B == None:
        return []
    else:
        q = queue.Queue()
        q.enqueue(B)
        q.enqueue(None)
        s = 0       # the sum of keys
        cpt = 0     # nb of keys
        res = []
        while not q.isempty():
            B = q.dequeue()
            if B == None:
                res.append(s/cpt)
                if not q.isempty():
                    q.enqueue(None)
                    s = 0
                    cpt = 0
            else:
                s = s + B.key
                cpt = cpt+1
                if B.left != None:
                    q.enqueue(B.left)
                if B.right != None:
                    q.enqueue(B.right)
        return res
        
# another way to manage levels, with two queues.                    
def get_average2(B): 
    '''
    B: bintree
    builds and returns the list L:
    - len(L) = number of levels of the binary tree
    - L[i] = average of the key values at level i
    '''
    res = []
    if B != None:
        q = queue.Queue() #current
        q.enqueue(B)
        q_next = queue.Queue() #next level
        s = 0       
        cpt = 0     
        while not q.isempty():
            B = q.dequeue()
            s = s + B.key
            cpt = cpt+1
            if B.left != None:
                q_next.enqueue(B.left)
            if B.right != None:
                q_next.enqueue(B.right)
            if q.isempty():
                res.append(s / cpt)
                (q, q_next) = (q_next, q)
                (s, cpt) = (0, 0)
    return res

# -*- coding: utf-8 -*-
"""
S2 Matrices: maths and tests
"""

import matrix
#import timing

#------------------------------------------------------------------------------
#1.3 Addition

# first version: the result matrix is built before
def add_matrices(A, B):
    '''
    A, B: non-empty matrices
    returns the sum of matrices A and B
    '''
    (l, c) = (len(A), len(A[0]))
    if len(B) != l or len(B[0]) != c:
        raise Exception("add_matrices: Matrices do not have the same dimensions")
    M = matrix.init(l, c, 0)
    for i in range(l):
        for j in range(c):
            M[i][j] = A[i][j] + B[i][j]
    return M

# second version: the result matrix is built as we go along
def add_matrices2(A, B):
    '''
    A, B: non-empty matrices
    returns the sum of matrices A and B
    '''
    (l, c) = (len(A), len(A[0]))
    if (l, c) != (len(B), len(B[0])):
        raise Exception("add_matrices2: Matrices do not have the same dimensions")
    M = []
    for i in range(l):
        L = []
        for j in range(c):
            L.append(A[i][j] + B[i][j])
        M.append(L)
    return M

#------------------------------------------------------------------------------
#1.4 Product
    
def mult_matrices(A, B):
    '''
    A, B: non-empty matrices
    returns the product of matrices A and B
    '''
    m = len(A)
    n = len(A[0])
    if n != len(B):
        raise Exception("mult_matrices: incompatible dimensions")
    p = len(B[0])
    M = matrix.init(m, p, 0)
    for i in range(m):
        for j in range(p):
            for k in range(n):
                M[i][j] = M[i][j] + A[i][k] * B[k][j]
    return M

#------------------------------------------------------------------------------
#2.1 Maximum gap

def gaplist(L, n):
    '''
    L: non-empty list
    n: size of the list L
    returns the gap of L
    '''
    valMin = L[0]
    valMax = L[0]
    for i in range(1, n):
        valMin = min(valMin, L[i])
        valMax = max(valMax, L[i])
    return valMax - valMin

def maxGap(M):
    '''
    M: non-empty matrix
    returns the gap of M
    '''
    c = len(M[0])
    mgap = gaplist(M[0], c)
    for i in range(1, len(M)):
        mgap = max(mgap, gaplist(M[i], c))
    return mgap


# in one function (gaplist inlined)
def maxGap(M):
    '''
    M: non-empty matrix
    returns the gap of M
    '''
    mgap = 0
    (l, c) = (len(M), len(M[0]))
    for i in range(l):
        valMin = M[i][0]
        valMax = M[i][0]
        for j in range(1, c):
            valMin = min(valMin, M[i][j])
            valMax = max(valMax, M[i][j])
        mgap = max(mgap, valMax - valMin)
    return mgap
    

#------------------------------------------------------------------------------
#2.2 Symmetry

def symmetric(A):
    '''
    A: non-empty matrix
    returns True if A is symmetric, False otherwise
    '''
    (l, c) = (len(A), len(A[0]))
    if l != c:
        raise Exception("symmetric: not a square matrix")
    i = 0
    j = -1
    while i < l and j == (i-1):
        j = 0
        while j < i and A[i][j] == A[j][i]:
            j += 1
        i += 1
    return i == l and j == (i-1)
    
#------------------------------------------------------------------------------
#2.3 Sorted matrix
def list_sorted(L, n):
    '''
    L: non-empty list
    n: size of L
    returns True if L is in increasing order, False otherwise
    '''
    i = 1
    while i < n and L[i-1] <= L[i]:
        i = i + 1
    return i == n

def matrix_sorted(M):
    '''
    L: non-empty list
    n: size of L
    returns True if M is sorted, False otherwise
    '''
    if not list_sorted(M[0], len(M[0])):
        return False
    else :
        c = len(M[0])
        l = len(M)
        i = 1
        while i < l and M[i-1][c-1] < M[i][0] and list_sorted(M[i], c):
            i = i + 1
        return i == l

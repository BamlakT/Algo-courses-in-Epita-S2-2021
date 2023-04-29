# -*- coding: utf-8 -*-
"""
Philosophers Stone
S2 - Matrix tutorial
"""

from algopy import matrix
from algopy import timing

# uncomment the lines @timing.timing if you want to see the durations!


##### Helpers
def posmax(L):
    '''
    position of (one of) the maximum value in list L, non empty
    '''
    pos = 0
    for i in range(1, len(L)):
        if L[i] > L[pos]:
            pos = i
    return pos

def reverse(L):
    """
    reverse L in place
    """
    n = len(L)
    for i in range(n//2):
        (L[i], L[n-i-1]) = (L[n-i-1], L[i])
        
#----------------- Greedy Algorithm (algorithme glouton) ----------------------

# matrices are assumed not empty in all the following functions

@timing.timing
def HarryPotter_greedy(T):
    col = len(T[0])
    j = posmax(T[0])
    s = T[0][j]
    for i in range(1, len(T)):
        jmax = j
        if j > 0 and T[i][j-1] > T[i][jmax]:
            jmax = j-1
        if j < col-1 and T[i][j+1] > T[i][jmax]:
            jmax = j+1
        j = jmax
        s += T[i][j]
    return s

# with the path
def HarryPotterGreedy_path(T):
    col = len(T[0])
    j = posmax(T[0])
    s = T[0][j]
    way = [j]
    for i in range(1, len(T)):
        jmax = j
        if j > 0 and T[i][j-1] > T[i][jmax]:
            jmax = j-1
        if j < col-1 and T[i][j+1] > T[i][jmax]:
            jmax = j+1
        j = jmax
        way.append(j)
        s += T[i][j]
    return (s, way)

#----------------- Dynamic Programming ----------------------


def build_max_matrix(T):
    l = len(T)
    c = len(T[0])
    M = matrix.init(l, c, 0)
    
    # copy the first line
    for j in range(c):
        M[0][j] = T[0][j]

    for i in range(1, l):
        M[i][0] = T[i][0] + max(M[i-1][0], M[i-1][1])
        for j in range(1, c-1):
            M[i][j] = T[i][j] + max(M[i-1][j-1], M[i-1][j], M[i-1][j+1])
        M[i][c-1] = T[i][c-1] + max(M[i-1][c-2], M[i-1][c-1])
    
    return M
    
@timing.timing
def HarryPotter(T):
    M = build_max_matrix(T)
    n = len(M)  # line nb
    return M[n-1][posmax(M[n-1])]

# with the path    
def HarryPotter_path(T):
    M = build_max_matrix(T)
    (l, c) = (len(M), len(M[0]))  
    
    # build the path: going-up in M
    j = posmax(M[l-1])
    val = M[l-1][j]
    path = [j]
    for i in range(l-2, -1, -1):
        jmax = j
        if j > 0 and M[i][j-1] > M[i][jmax]:
            jmax = j-1
        if j < c-1 and M[i][j+1] > M[i][jmax]:
            jmax = j+1
        j = jmax
        path.append(j)
    reverse(path)
    return (val, path)
    

#----------------------------------------------------------------------
# Brut force... warning: can be long when l, c >= 15, 15

# without the path
def brut(T, i, j):
    if i == len(T)-1:
        return T[i][j]
    else:
        m = brut(T, i+1, j)
        if j > 0:
            mleft = brut(T, i+1, j-1)
            if mleft > m:
                m = mleft
        if j < len(T[0]) - 1:
            mright = brut(T, i+1, j+1)
            if mright > m:
                m = mright
        return (m + T[i][j])

@timing.timing
def HarryPotter_brutforce(T):
    
    maxi = 0
    for j in range(len(T[0])):
        maxi = max(maxi, brut(T, 0, j))
    return maxi


#      BONUS: brut force with the path           

# the list is returned (use + the concatenate...)
def brut_path(T, i, j):
    if i == len(T)-1:
        return (T[i][j], [j])
    else:
        (m, L) = brut_path(T, i+1, j)
        if j > 0:
            (mleft, Lleft) = brut_path(T, i+1, j-1)
            if mleft > m:
                m = mleft
                L = Lleft
        if j < len(T[0]) - 1:
            (mright, Lright) = brut_path(T, i+1, j+1)
            if mright > m:
                m = mright
                L = Lright
        return (m + T[i][j], [j] + L)


def HarryPotter_brutforce_path(T):
    
    maxi = 0
    for j in range(len(T[0])):
        (m, L) = brut_path(T, 0, j)
        if m > maxi:
            (maxi, Lmax) = (m, L)
    return (maxi, Lmax)



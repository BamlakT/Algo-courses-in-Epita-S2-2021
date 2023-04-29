# -*- coding: utf-8 -*-
"""
Magic Squares
@author: Nathalie
"""

from algopy import matrix

# moves : [+1, +1], [-1, 0]
# assume      n is odd > 2


# first version : test if cell is empty -> if not move [-1, 0]
def Siamese_(n):
    """
    n: odd size of the siamese square
    builds and returns a magic square of n-odd size
    starts in the middle of last line, then going SE
    """
    S = matrix.init(n, n, 0)
    i = n-1
    j = n // 2
    S[i][j] = 1
    for k in range(2, n*n + 1):
        i2 = (i + 1) % n
        j2 = (j + 1) % n
        if S[i2][j2] == 0:
            (i, j) = (i2, j2)
        else:
            i = i-1
            if i == -1:
                i = n-1
        S[i][j] = k
    return S

# second version: change direction each n*k +1
def Siamese(n):
    """
    n: odd size of the siamese square
    builds and returns a siamese square of odd size n
    """
    S = matrix.init(n, n, 0)
    (i, j) = (n - 1, n // 2)
    for val in range(1, n*n + 1):
        S[i][j] = val
        if val % n == 0:
            i = i - 1
            if i == -1:
                i = n-1
        else:
            (i, j) = ((i + 1) % n, (j + 1) % n)
    return S


# second version
def Siamese2(n):
    """
    n: odd size of the siamese square
    builds and returns a siamese square of odd size n
    """
    M = matrix.init(n, n, 0)
    (i, j) = (n - 1, n // 2)
    M[i][j] = 1
    for val in range(2, n*n+1):
        if (val-1) % n == 0:
            if i == 0:
                i = n - 1
            else:
                i = i - 1
        else:
            (i, j) = ((i + 1) % n, (j + 1) % n)
        M[i][j] = val
    return M

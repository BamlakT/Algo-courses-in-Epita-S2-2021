# -*- coding: utf-8 -*-
"""
Matrices: classics
"""


#------------------------------------------------------------------------------
# 1.1 Displays

def printmat(M):
    '''
    M: matrix
    prints the matrix M, elements of a line separated by a space,
    lines separated by a linebreak
    '''
    for line in M:
        for el in line:
            print(el, end=' ')
        print()
    
def prettyprint(M, d=0):
    '''
    M: non-empty matrix
    d: size of the cells
    print the matrix M
    '''
    c = len(M[0])
    if d == 0:
        for line in M:
            for e in line:
                d = max(d, len(str(e)))
    line = ""
    for i in range(c*(d+3)+1):
        line = line + '-'
    for i in range(len(M)):
        print(line)
        for j in range(c):
            s = "| {:" + str(d) + "d}"
            print(s.format(M[i][j]), end=' ')
        print('|')
    print(line)

#------------------------------------------------------------------------------
# 1.2 Init

def init(l, c, val):
    '''
    l: number of lines
    c: number of columns
    val: value
    initializes and returns a l x c matrix full of "val"
    '''
    res = []
    for i in range(l):
        line = []
        for j in range(c):
            line.append(val)
        res.append(line)
    return res

#------------------------------------------------------------------------------
# 1.2 Load

def __str2intlist(s):
    '''
    s: string containig a line of the matrix
    converts and returns s into a line of the matrix
    '''
    L = []
    (i, n) = (0, len(s))
    while i < n:
        word = ""
        while i < n and s[i] != ' ' and s[i] != '\n':
            word += s[i]
            i += 1
        L.append(int(word))
        i += 1
    return L

def load(filename):
    '''
    filename: name of the file containing the matrix
    loads a matrix from the text file filename
    '''
    f = open(filename)
    lines = f.readlines()
    f.close()
    M = []
    for line in lines:
        M.append(__str2intlist(line))
    return M
        
#------------------------------------------------------------------------------

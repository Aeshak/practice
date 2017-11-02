# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
alls = 0
def explore(i,j,m,n):
    global alls
    alls += 1
    #print (i, j)
    #return
    if i < n-1:
        v = m[i+1][j]
        m[i+1][j] = 'X'
        if v == '1':
            explore(i+1,j,m,n)
    if i < n-1 and j < n-1 :
        v = m[i+1][j+1]
        m[i+1][j+1] = 'X'
        if v == '1':
            explore(i+1,j+1,m,n)
    if i < n-1 and j > 0:
        v = m[i+1][j-1]
        m[i+1][j-1] = 'X'
        if v == '1':
            explore(i+1,j-1,m,n)
    if j < n-1:
        v = m[i][j+1]
        m[i][j+1] = 'X'
        if v == '1':
            explore(i,j+1,m,n)
    if j > 0:
        v = m[i][j-1]
        m[i][j-1] = 'X'
        if v == '1':
            explore(i,j-1,m,n)
    if i > 0:
        v = m[i-1][j]
        m[i-1][j] = 'X'
        if v == '1':
            explore(i-1,j,m,n)
    if i > 0 and j < n-1:
        v = m[i-1][j+1]
        m[i-1][j+1] = 'X'
        if v == '1':
            explore(i-1,j+1,m,n)
    if i > 0 and j > 0:
        v = m[i-1][j-1]
        m[i-1][j-1] = 'X'
        if v == '1':
            explore(i-1,j-1,m,n)

#h = open("Bumble.in", 'r')
#content = h.read().split("\n")
#h.close()
#h = open("Bumble.out", 'w')
content = sys.stdin.readlines()
f = 0
imgNo = 0
while f < len(content):
    imgNo += 1
    n = int(content[f])
    f += 1
    m = [None]*n
    for l in range(n):
        m[l] = list(content[f])
        f += 1
    i = j = 0
    count = 0
    for i in range(n):
        for j in range(n):
            #res = None
            if m[i][j] == '1':
                explore(i,j,m,n)
                m[i][j] = '1'
                count += 1
    #h.write("Image number %d contains %d war eagles.\n" %(imgNo,count))
    print("Image number %d contains %d war eagles." %(imgNo,count))
#print alls
#h.close()


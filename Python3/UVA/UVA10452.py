# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 23:42:07 2017

@author: aeshak
"""

def explore(i,j,s,m,n,out,mode,loc = 0):
    global cons
    if i < m-1:
        v = s[i+1][j]
        s[i+1][j] = 'X'
        if loc < 7 and v == cons[loc]:
            out.append("forth")
            loc += 1
            explore(i+1,j,s,m,n,out,mode,loc)
    if j < n-1:
        v = s[i][j+1]
        s[i][j+1] = 'X'
        if loc < 7 and v == cons[loc]:
            out.append("right")
            loc += 1
            explore(i,j+1,s,m,n,out,mode,loc)
    if j > 0:
        v = s[i][j-1]
        s[i][j-1] = 'X'
        if loc < 7 and v == cons[loc]:
            out.append("left")
            loc += 1
            explore(i,j-1,s,m,n,out,mode,loc)
    if i > 0:
        v = s[i-1][j]
        s[i-1][j] = 'X'
        if loc < 7 and v == cons[loc]:
            out.append("forth")
            loc += 1
            explore(i-1,j,s,m,n,out,mode,loc)

cons = "IEHOVA#"
t  = int(input())
allOut = list()
for x in range(t):
    m,n = map(int,input().split())
    s = [None]*m
    start = (0,0)
    end   = (m,n)
    out = list()
    for i in range(m):
        s[i] = list(input())
        if '#' in s[i]:
            end = (i,s[i].index("#"))
        if '@' in s[i]:
            start = (i,s[i].index("@"))
    mode = 0
    explore(start[0],start[1],s,m,n,out,mode)
    allOut.append(out)
for i in allOut:
    print(" ".join(i))

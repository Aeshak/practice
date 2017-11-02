# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 15:47:03 2017

@author: aeshak
"""
import sys
sys.setrecursionlimit(5000)

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def isValid(i,j,n,m):
   return i>=0 and j>=0 and i<n and j<m

def doexplore(color,i,j,n,m,a,visited,parent):
    visited[i][j] = color
    for x in range(4):
        r = dr[x]
        c = dc[x]
        nn = i+r
        mm = j+c 
        if isValid(nn,mm,n,m) and a[nn][mm] == color:
            if visited[nn][mm] != color:
                if doexplore(color,nn,mm,n,m,a,visited,(i,j)):
                    return True
            elif parent != (nn,mm):
                return True
    return False

def explore(color,i,j,n,m,a,visited):
    if visited[i][j] != color:
        return doexplore(color,i,j,n,m,a,visited,(i,j))
    return False
n,m = map(int,raw_input().split())

a = [None]*n
for i in range(n):
   a[i] = list(raw_input())

visited = [[None]*m for i in range(n)]

atLeastOneFound = False
for i in range(n):
    for j in range(m):
        if explore(a[i][j],i,j,n,m,a,visited):
            print("Yes")
            atLeastOneFound = True
            break
    if atLeastOneFound:
        break
if not atLeastOneFound:
    print("No")

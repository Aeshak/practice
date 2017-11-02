# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 13:03:26 2017

@author: aeshak
"""
import sys
sys.setrecursionlimit(100000)

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def isValid(i,j,n,m):
	return i>=0 and j>=0 and i < n and j < m

def dfs(B,i,j,n,m,visited):
	visited[i][j] = True
	for x in range(4):
		ni = i+dr[x]
		nj = j+dc[x]
		if isValid(ni,nj,n,m):
			if not visited[ni][nj] and (B[ni][nj] == 'x' or B[ni][nj] == '@'):
				dfs(B,ni,nj,n,m,visited)
T = int(input())
out = ""
for _ in range(1,T+1):
	n = int(input())
	B = [None]*n
	visited = [None]*n
	for i in range(n):
		B[i] = list(input())
		visited[i] = [False]*n
	a = 0
	for i in range(n):
		for j in range(n):
			if not visited[i][j] and B[i][j] == 'x':
				a += 1
				dfs(B,i,j,n,n,visited)
	out += "Case %d: %d\n"%(_,a)
print(out.rstrip())

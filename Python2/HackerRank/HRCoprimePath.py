#!/bin/python

import sys
from collections import defaultdict

def gcd(x,y):
	if x == y:
		return x
	if x > y:
		return gcd(x-y,y)
	return gcd(x,y-x)

def dfs(g,nodes,u,v,n,visited,count):
	if u == v:
		return True
	visited[u-1] = True
	for i in g[u]:
		if not visited[i-1]:
			count.append(i)
			return dfs(g,nodes,i,v,n,visited,count)
	count = list()
	return False

n,q = map(int,raw_input().strip().split(' '))
nodes = map(int,raw_input().strip().split(' '))
g = defaultdict(list)
for edges_i in xrange(n-1):
	a,b = map(int,raw_input().strip().split(' '))
	g[a].append(b)
	g[b].append(a)
#print g
for a0 in xrange(q):
	u,v = map(int,raw_input().strip().split(' '))
	#u = int(raw_input().strip())
	#v = int(raw_input().strip())
	count = list()
	count.append(u)
	visited = [False]*n
	dfs(g,nodes,u,v,n,visited,count)
	l = len(count)
	t = 0
	for i in xrange(l):
		for j in xrange(i+1,l):
			if gcd(nodes[count[i]-1],nodes[count[j]-1]) == 1:
				t+=1
	print t

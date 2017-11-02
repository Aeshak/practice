# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 18:08:18 2017

@author: aeshak
"""
import sys
sys.setrecursionlimit(20000)

from collections import defaultdict

class Graph:
	
	def __init__(self,V):
		self.V = V
		self.graph = defaultdict(list)
		self.count = 0
	
	def addEdge(self,v,w):
		self.graph[v].append(w)
		self.graph[w].append(v)
	
	def cycleUtil(self,v,visited,parent = -1):
		visited[v] = True
		if parent == -1:
			self.count = 1
		for i in self.graph[v]:
			if not visited[i]:
				if self.cycleUtil(i,visited,v):
					self.count += 1
					return True
			elif parent != i:
				return True
		return False
		
	def cycle(self):
		visited = [False]*self.V
		toRemove = 0
		for i in range(self.V):
			if not visited[i]:
				if self.cycleUtil(i,visited):
					#print self.count
					if self.count != 1 and self.count%2 == 1:
						toRemove += 1
		return toRemove

n,m = map(int, raw_input().split())
g = Graph(n)
for _ in range(m):
	v,w = map(int, raw_input().split())
	g.addEdge(v-1,w-1)
toRemove = g.cycle()
if (n-toRemove)%2 == 1:
	toRemove += 1
print toRemove



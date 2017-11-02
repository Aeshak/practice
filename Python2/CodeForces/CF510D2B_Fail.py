# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 01:44:24 2017

@author: aeshak
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 23:42:07 2017

@author: aeshak
"""
def isValid(i,j,n,m):
   return i >=0 and j >=0 and i < n and j < m
delta = [(0,1),(0,-1),(-1,0),(1,0)]
def adjacent(t1,t2):
   if (abs(t1[0]-t2[0])+abs(t1[1]-t2[1])) == 1:
      return True
   return False
def isCyclicUtil(v,visited,parent,graph):
   #Mark the current node as visited 
   visited[v]= True
 
   #Recur for all the vertices adjacent to this vertex
   for i in graph:
      # If the node is not visited then recurse on it
      if  visited[i]==False and adjacent(i,v): 
         if isCyclicUtil(i,visited,v,graph):
            return True
         elif  parent!=i:
            # If an adjacent vertex is visited and not parent of current vertex,
            # then there is a cycle
            return True
   return False

def cycleTest(isAndJs,n,m,k):
#   V = len(isAndJs)
   visited = dict.fromkeys(isAndJs, False)
   for i in isAndJs:
      if visited[i] == False: #Don't recur for u if it is already visited
         if(isCyclicUtil(i,visited,-1,isAndJs))== True:
            return True
   return False
   
n,m = map(int,raw_input().split())
a = [None]*n
colors = dict()
for i in range(n):
   a[i] = list(raw_input())
   for j in range(m):
      if colors.has_key(a[i][j]):
         colors[a[i][j]].append((i,j))
      else:
         colors[a[i][j]] = [(i,j)]
atLeastOneFound = False
for key in colors.keys():
   if len(colors[key]) >= 4:
      if cycleTest(colors[key],n,m,-1):
         print("Yes")
         atLeastOneFound = True
         break
if not atLeastOneFound:
   print("No")   

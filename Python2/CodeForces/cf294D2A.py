# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 16:04:57 2017

@author: aeshak
"""

n = int(raw_input())
A = map(int, raw_input().split())
m = int(raw_input())
for i in range(m):
   x,y = map(int, raw_input().split())
   # 0 to y-1 left birds
   # y+1 to A[x-1] right birds 
   lbirds = y-1 
   rbirds = A[x-1] - y
   if x-1 != 0:
      A[x-2] += lbirds
   if x != n:
      A[x] += rbirds
   A[x-1] = 0
for i in A:
   print i

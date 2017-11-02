# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 02:25:48 2017

@author: aeshak
"""

n = int(raw_input())
A = range(1,n+1)
s = 0
for i in range(pow(2,n)):
   x = bin(i)[2:]
   x = '0'*(n-len(x))+x
   for j in range(n):
      if x[j] == '1':
         s += A[j]
print s

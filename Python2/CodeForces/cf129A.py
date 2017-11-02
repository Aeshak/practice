# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:20:20 2017

@author: aeshak
"""
n = int(raw_input())
A = map(int, raw_input().split())
s = sum(A)
count = 0
for i in A:
   if (s-i)%2 == 0:
      count +=1
print count

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 03:46:59 2017

@author: aeshak
"""
t = int(raw_input())
for i in range(t):
   n = int(raw_input())
   # Calc This formula [(n*(n+1))/2]*2^(n-1)
   s = n*(n+1)/2
   s = s*pow(2,n-1)
   print s

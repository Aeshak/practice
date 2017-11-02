# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:52:50 2017

@author: aeshak
"""

n = int(raw_input())
A = map(int,raw_input().split())
A.sort()
m = min(A)
flag = 0
for i in A:
   if i > m:
      flag = 1
      print i
      break
if flag == 0:
   print "NO"

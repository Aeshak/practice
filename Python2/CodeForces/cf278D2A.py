# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 22:34:39 2017

@author: aeshak
"""
def calc(a,b,d,n):
   if a == b:
      print 0
      return   
   out1 = 0
   for i in range(a-1,b-1):
      out1 += d[i]
   out2 = 0
   for i in range(0,a-1):
      out2 += d[i]
   for i in range(b-1,n):
      out2 += d[i]   
   out = min(out1,out2)
   print(out)

n = int(raw_input())
d = map(int,raw_input().split())
s = map(int,raw_input().split())
a = min(s)
b = max(s)
calc(a,b,d,n)

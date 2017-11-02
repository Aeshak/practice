# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 15:47:58 2017

@author: aeshak
"""
n = int(raw_input())
num = 0
for i in range(n):
   h,b,a = raw_input().split()
   b,a = map(int, (b,a))
   if a > b and b >= 2400:
      num += 1
if num > 0:
   print "YES"
else:
   print "NO"

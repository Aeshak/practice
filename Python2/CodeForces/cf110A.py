# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 15:03:43 2017

@author: aeshak
"""

n = raw_input()

num = 0
for i in n:
   if i == '4' or i == '7':
      num += 1
flag = True
for i in str(num):
   if i != '4' and i != '7':
      flag = False
if flag:
   print "YES"
else:
   print "NO"

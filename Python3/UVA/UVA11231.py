# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 02:18:41 2017

@author: aeshak
"""

while True:
   n,m,c = map(int,input().split())
   if n == m == c == 0:
      break
   print (int(((n-7)*(m-7)+c)/2))

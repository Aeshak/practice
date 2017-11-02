# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 21:58:15 2017

@author: aeshak
"""

n,t = map(int, raw_input().split())
if t == 10 and n == 1:
	print -1
elif t == 10:
	print pow(10,n-2)*t
else:
	print pow(10,n-1)*t
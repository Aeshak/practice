# -*- coding: utf-8 -*-
"""
Created on Fri Sep 01 02:45:27 2017

@author: aeshak
"""

n,m = map(int,raw_input().split())
i = 1
x = n
while x > 0:
	x -= 1
	if i%m == 0:
		x += 1
	i += 1
print i-1
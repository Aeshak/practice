# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 23:18:28 2017

@author: aeshak
"""
n = input()
A = map(int,raw_input().split())
mind = 1000000000000
for i in xrange(1,n-1):
	B = A[0:i] + A[i+1:]
	d = list()
	for j in xrange(1,n-1):
		d.append(abs(B[j-1]-B[j]))
	mind = min(max(d),mind)
print mind
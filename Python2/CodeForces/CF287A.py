# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 22:34:30 2017

@author: aeshak
"""
def valid(i,j,n):
	return i >= 0 and i+1 < n and j >= 0 and j+1 < n
n = 4
A = [""]*n
for i in xrange(n):
	A[i] = raw_input()
found = False
for i in xrange(n):
	for j in xrange(n):
		if valid(i,j,n):
			hc = dc = 0
			for k in xrange(i,i+2):
				for l in xrange(j,j+2):
					if A[k][l] == "#":
						hc += 1
					elif A[k][l] == ".":
						dc += 1
			if hc <= 1 or dc <= 1:
				print "YES"
				found = True
				break
	if found:
		break
if not found:
	print "NO"

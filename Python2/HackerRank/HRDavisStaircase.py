#!/bin/python

import sys

def combinations(s,n,count):
	s1 = sum(int(_) for _ in s)
	if s1 == n:
		count[0] +=1
		return s
	if s1 > n:
		return s
	return combinations(s+'1',n,count)+combinations(s+'2',n,count)+combinations(s+'3',n,count)

#s = int(raw_input().strip())
s = 1
steps = range(1,21)
for _ in xrange(s):
	#n = int(raw_input().strip())
	n = 21
	count = [0]
	combinations('',n,count)
	print count[0]

 
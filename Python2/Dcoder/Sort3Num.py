import sys
a,b,c = map(int,raw_input().split())
if a > b:
	a,b = b,a
if b > c:
	b,c = c,b
if a > c:
	a,c = c,a
if a > b:
	a,b = b,a
print str(a)+" "+str(b)+" "+str(c)
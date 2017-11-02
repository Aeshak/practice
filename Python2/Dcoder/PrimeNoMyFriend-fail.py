import math
import sys

def sieve(n):
	A = [1]*n
	A[0] = 0
	A[1] = 0
	for i in range(2,int(math.sqrt(n))):
		if A[i] == 1:
			j = i*i
			while j < n:
				A[j] = 0
				j += i
	B = []
	for i in range(len(A)):
		if A[i] == 1:
			B.append(i)
	return B
# solution for n = 200000*ln(n)
A = sieve(600)
n = int(raw_input())
t = n
low = 0
hi = len(A)-1
while low <= hi:
	s = A[low]+A[hi]
	if s < t:
		low += 1
	else:
		if s == t:
			print str(A[low])+" "+str(A[hi])
		hi -= 1

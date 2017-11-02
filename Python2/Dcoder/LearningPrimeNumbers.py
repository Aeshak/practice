import math
import sys

def sieve(n):
	A = [1]*n
	A[0] = 0
	A[1] = 0
	for i in range(2,int(math.sqrt(n))+1):
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
A = sieve(10000000)
#print A[-1]
#print len(A)
a,b = map(int,raw_input().split())
for i in range(len(A)):
	if A[i] >= a and A[i] <= b:
		print A[i]
    
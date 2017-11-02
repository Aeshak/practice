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

n = int(raw_input())
A = sieve(n)
st = 0
en = len(A)-1
while st < en:
	sum = A[st] + A[en]
	if sum > n:
		en -= 1
	elif sum < n:
		st += 1
	else:
		sys.stdout.write(str(A[st])+" "+str(A[en])+"\n")
		st += 1
		en -= 1
sys.stdout.flush()
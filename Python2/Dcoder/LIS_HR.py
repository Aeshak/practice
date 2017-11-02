#python 2.7.6
import math
N = int(raw_input())
X = [None]*N
for i in range(N):
	X[i] = int(raw_input())
#X = map(int, raw_input().split())
P = [None]*N
M = [None]*(N+1)
L = 0 
for i in range(N):
	lo = 1
	hi = L
	while lo <= hi:
		mid = int(math.ceil((lo+hi)/2))
		if X[M[mid]] < X[i]:
			lo = mid+1
		else:
			hi = mid-1 
	newL = lo
	P[i] = M[newL-1]
	M[newL] = i
	if newL > L:
		L = newL 
#print P
#print M
S = [None]*L
k = M[L]
for i in reversed(range(L)): 
	S[i] = X[k]
	k = P[k]
#print " ".join(map(str,S))
print len(S)
    
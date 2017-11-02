N,M = map(int,raw_input().strip().split())
m = pow(10,9)+7
A = map(int,raw_input().strip().split())
B = map(int,raw_input().strip().split())
C = map(int,raw_input().strip().split())
A.insert(0,0)
B.insert(0,0)
C.insert(0,0)
for i in xrange(1,M+1):
	for j in xrange(1,N+1):
		if j % B[i] == 0:
			A[j] = A[j] * C[i]
print A
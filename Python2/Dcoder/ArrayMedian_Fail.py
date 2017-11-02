n = int(raw_input())
A = map(int,raw_input().split())
print sum(A)/n
"""
A.sort()
if n%2 == 0:
	print A[n/2]
else:
	print A[(n+1)/2]
"""
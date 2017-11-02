#import sys
#n = int(raw_input())
#A = map(int,raw_input().split())
A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

#A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
n = len(A)
m = mt = A[0]
B = [0]*n
k = 1
for i in range(1,n):
	if m < A[i-1]:
		B[k] = m
		k+=1
	"""
	m = min(m,A[i])
	mt = max(m,mt)
	m = A[i]
	B[i] = mt
	"""
"""
for i in sorted(B):
	sys.stdout.write(str(i)+" ")
"""
print(B)
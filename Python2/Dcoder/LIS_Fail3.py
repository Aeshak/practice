#import sys
#n = int(raw_input())
#A = map(int,raw_input().split())
A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

#A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
n = len(A)
L = [[None] for i in range(n)]
for i in range(n):
	for j in range(i,n):
		end = L[i][-1]
		if end is None:
			L[i][-1] = A[i]
		if end > A[j]:
			L[i][-1] = A[j]
		if L[i][-1] < A[j]:
			L[i].append(A[j])
print L
			
    
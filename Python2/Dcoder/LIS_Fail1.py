n = int(raw_input())
#A = map(int,raw_input().split())
#A = [8, 0, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
#A = [2, 5, 3, 7, 11, 8, 7, 9]
#print A
#n = len(A)
A = []
for i in range(n):
	A.append(int(raw_input()))
prev = [A[0]]
k = 1
for i in A:
	nprev = len(prev)
	last = prev[nprev-1]
	if i > last:
		prev.append(i)
	else:
		if nprev == 1 and last > i:
			prev[nprev-1] = i
		if nprev != 1 and i > prev[nprev-2]:
			prev[nprev-1] = i
	#print prev
print(len(prev))
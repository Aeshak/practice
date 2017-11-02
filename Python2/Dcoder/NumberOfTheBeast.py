n = int(raw_input())
A = map(str,raw_input().split())
for i in range(len(A)):
	if A[i] != "0" and int(A[i])%6 == 0:
		A[i] = "*"*len(A[i])
print " ".join(A)

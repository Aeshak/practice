import sys
t = int(raw_input())
for i in range(t):
	n,x,y = map(int,raw_input().split())
	A = []
	d = 1
	z = x
	while n > z:
		A.append(z)
		d += 1
		z = d*x
	d = 1
	z = y
	while n >= z:
		z = d*y
		if z in A:
			A[A.index(z)] = -1
		d += 1
	for i in range(len(A)):
		if A[i] > 0:
			sys.stdout.write(str(A[i]))
			if i != len(A)-1:
				sys.stdout.write(" ")
	sys.stdout.write("\n")
	sys.stdout.flush()
	
    
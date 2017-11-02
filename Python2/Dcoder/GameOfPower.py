t = int(raw_input())
for i in range(t):
	n = int(raw_input())
	if n < 3:
		print n-1
		continue
	b = 2
	A = [4]
	x = 4
	while x < n:
		e = 2
		x = pow(b,e)
		A.append(x)
		y = x
		while y < n:
			y = pow(b,e)
			A.append(y)
			e += 1
		b += 1
	#print A
	if n in A:
		print 0
	else:
		A = map(lambda x: abs(n-x),A)
		print min(A)

    

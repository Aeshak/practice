def nextFibo(n):
	xn_2, xn_1, xn = 0,1,1
	if n==0:
		return 1
	if n==1:
		return 2
	while n >= xn:
		xn = xn_1+xn_2
		xn_2 = xn_1
		xn_1 = xn
	return xn
t = int(raw_input())
for i in range(t):
	n = int(raw_input())
	print nextFibo(n)


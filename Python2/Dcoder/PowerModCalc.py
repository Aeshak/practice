def fpow(x,n,m):
	if n==0:
		return 1
	if n%2 == 0:
		y = fpow(x%m,n/2,m)
		y = y%m
		return (y*y)%m
	z = fpow(x%m,n-1,m)
	z = z%m
	return (z*(x%m))%m
t = int(raw_input())
for i in range(t):
	x,n,m = raw_input().split(" ")
	x,n,m = int(x),int(n),int(m)
	print(str(fpow(x,n,m)))
import math
def fpow(x,n):
	if n==0:
		return 1
	if n%2 == 0:
		y = fpow(x,n/2)
		return (y*y)
	return x*fpow(x,n-1)
t = int(raw_input())
for i in range(t):
	n = int(raw_input())
	for i in range(int(math.sqrt(n))+2):
		sqr = fpow(i,2)
		if sqr > n:
			print(abs(fpow(i-1,2)-n))
			break
		if sqr == n:
			print(0)
			break
    
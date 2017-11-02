def gcd(x,y):
	if x == y:
		return x
	if x > y:
		return gcd(x-y,y)
	return gcd(x,y-x)

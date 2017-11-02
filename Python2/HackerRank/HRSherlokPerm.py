from math import factorial as fct
t = input()
for i in xrange(t):
	n,m = map(int,raw_input().split())
	a = n+m-1
	# ncr = n!/(r!(n-r)!) n is a r is m-1
	r = m-1
	res = fct(a)/(fct(r)*fct(a-r))
	print res%1000000007
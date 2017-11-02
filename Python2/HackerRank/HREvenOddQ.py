N = input()
A = map(int,raw_input().split())
Q = input()
for i in xrange(Q):
	x,y = map(int,raw_input().split())
	if x == N or x == y:
		print "Even" if A[x-1]%2 == 0 else "Odd"
		continue
	if x > y:
		print "Odd"
		continue
	if A[x-1]%2 == 0 and A[x] != 0:
		print "Even"
	else:
		print "Odd"
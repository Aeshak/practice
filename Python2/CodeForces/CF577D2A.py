n,x = map(int,raw_input().split())
count = 0
if x <= n:
	count += 1
for i in xrange(2,n+1):
	if i*n < x:
		continue
	if x%i == 0:
		count += 1
print count

n = input()
a = map(int,raw_input().split())
out = 10000000000
for j in xrange(1,n-1):
	amod = a[:j]+a[j+1:]
	diffs = []
	for i in xrange(1,n-1):
		diffs.append(abs(amod[i-1]-amod[i]))
	out = min(out,max(diffs))
print out

s = [1,1,2,4]
narr = [0]*37
narr[0] = 1
narr[1] = 1
narr[2] = 2
narr[3] = 4
for i in xrange(4,37):
	narr[i] = 2*narr[i-1] - narr[i-4]
s = int(raw_input().strip())
for a0 in xrange(s):
	n = int(raw_input().strip())
	print narr[n]

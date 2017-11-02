n = int(raw_input())
w = 2*(n/7)
r = n%7
if r == 6:
	w += 1
	r = 1
if r > 2:
	r = 2
print "%d %d"%(w,r+w)

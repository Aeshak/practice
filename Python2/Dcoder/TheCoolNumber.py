def isCool(n,k):
	bstr = bin(n)
	bn = len(bstr)
	count = 0
	if bn < 3:
		return False
	for i in range(bn):
		if i+2 < bn:
			if bstr[i] == "1" and bstr[i+1] == "0" and bstr[i+2] == "1":
				count+=1
	if count >= k:
		return True
	return False

t = int(raw_input())
for i in range(t):
	r,k = map(int,raw_input().split())
	count = 0
	for i in range(1,r+1):
		if isCool(i,k):
			count += 1
	print count
		
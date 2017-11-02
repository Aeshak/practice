n = int(raw_input())
s = map(int,raw_input().split())
inc = set()
dec = set()
prev = s[0]
first = 0
for i in s[1:]:
	if i > prev:
		inc.add(i)
		if first == 0:
			inc.add(prev)
	elif i < prev:
		dec.add(i)
		if first == 0:
			dec.add(prev)
	else:
		if i in inc and i not in dec:
			dec.add(i)
		elif i in dec and i not in inc:
			inc.add(i)
		elif first == 0:
			inc.add(i)
			dec.add(i)
	first = 1
	prev = i
if len(inc)+len(dec) == n:
	print "Yes"
else:
	print "No"
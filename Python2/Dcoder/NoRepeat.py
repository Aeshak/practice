s = raw_input()
d = dict()
for i in s:
	if i in d:
		d[i] += 1
	else:
		d[i] = 1
sn = ""
for i in s:
	if d[i] > 0:
		sn += i
		d[i] *= -1
print sn
		
import string

t = int(raw_input())
for i in range(t):
	ld = dict().fromkeys(string.ascii_lowercase,0)
	ud = dict().fromkeys(string.ascii_uppercase,0)
	na = [0]*256
	s = raw_input()
	for i in s:
		if i in ld.keys():
			ld[i] += 1
		elif i in ud.keys():
			ud[i] += 1
		else:
			na[ord(i)] += 1
	out = ""
	for i in range(256):
		if na[i] > 0:
			out += chr(i)*na[i]
	udv = ud.values()
	ldv = ld.values()
	for i,j in zip(sorted(ld.keys()),sorted(ud.keys())):
		if ud[j] > 0:
			out += j*ud[j]
		if ld[i] > 0:
			out += i*ld[i]
	print(out)
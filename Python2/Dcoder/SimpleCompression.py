import sys
s = raw_input()
st = 0
n = len(s)
s += " "
ns = ""
for i in range(n+1):
	if s[st] != s[i] or i == n:
		ns += s[st]
		if i-st != 1:
			ns += str(i-st)
		st = i
if len(ns) < n:
	print(ns)
else:
	print(s)
    
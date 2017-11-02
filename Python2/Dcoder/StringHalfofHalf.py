t = int(raw_input())
for i in range(t):
	s =raw_input()
	n = len(s)
	s = s[:n/2]
	if len(s) < 3:
		print s[0]
	else:
		print s[0]+s[2]
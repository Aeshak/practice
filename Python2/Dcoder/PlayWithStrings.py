t = int(raw_input())
for i in range(t):
	s = raw_input().split()
	out = ""
	for w in s:
		out += w[::-1]+" "
	print(out.strip())
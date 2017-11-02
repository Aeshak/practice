b = list(raw_input())
first = 0
for i in range(len(b)-1,-1,-1):
	if first == 0:
		if b[i] == "1":
			first = 1
		continue
	if b[i] == "1":
		b[i] = "0"
	else:
		b[i] = "1"
print int("".join(b),2)
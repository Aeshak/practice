n,h  = map(int, raw_input().split())
ai = map(int, raw_input().split())
count = 0
for i in ai:
	if i <= h:
		count += 1
	else:
		count += 2
print count

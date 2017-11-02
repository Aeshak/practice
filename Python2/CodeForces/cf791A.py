a,b = map(int,raw_input().split())
count = 0
while True:
	a *= 3
	b *= 2
	count += 1
	if a > b:
		print count
		exit()
ai = map(int, raw_input().split())
s = raw_input()
count = 0
for i in s:
	count += ai[int(i)-1]
print count

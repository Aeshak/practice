n = int(raw_input())
A = raw_input().split(" ")
d = dict()
for i in A:
	i = int(i)
	if i in d:
		d[i] += 1
	else:
		d[i] = 1
mm = -1
for i in d.keys():
	if d[i] > n/2:
		mm = i
		break
print(mm)
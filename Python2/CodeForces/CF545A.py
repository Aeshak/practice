#python 2.7.6
n = int(raw_input())
c = [2]*n
for i in range(n):
	m = raw_input().split()
	for j in range(n):
		if m[j] == '1':
			c[i] -= 1
		elif m[j] == '2':
			c[j] -= 1
		elif m[j] == '3':
			c[i] -= 1
			c[j] -= 1
out = ""
count = 0
for i in range(n):
	if c[i] > 0:
		count += 1
		out += str(i+1)+" "
print count
if count != 0:
	print out.rstrip()
		
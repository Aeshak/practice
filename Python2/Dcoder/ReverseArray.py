import sys

n = raw_input()
n = int(n)
y = raw_input()
A = y.split(" ")
count = 1
for i in A[::-1]:
	sys.stdout.write(i)
	if count != n:
		sys.stdout.write(" ")
	++count
sys.stdout.flush()
    
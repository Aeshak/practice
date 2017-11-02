# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
import re
import string

t = int(raw_input().strip())
for _ in xrange(t):
	n = int(raw_input().strip())
	passns = raw_input().strip().split(' ')
	originalLoginAttempt = raw_input().strip()
	d = defaultdict(list)
	for i in xrange(n):
		d[passns[i]] = str(i)
	left = originalLoginAttempt
	for passn in passns:
		left = re.sub(passn, d[passn], left)
	out = []
	sick = []
	print left
	for i in left:
		if i in string.lowercase:
			sick.append(i)
		else:
			if len(sick) == 0:
				out.append(passns[int(i)])
			elif len(out) != 0:
				maybe = out.pop()+"".join(sick)
				if maybe in passns:
					out.append(maybe)
					sick = []
					out.append(passns[int(i)])
				print maybe
				print out
			else:
				out = []
				break
	print out
	print sick
	if len(out) != 0:
		print " ".join(out)
	else:
		print "WRONG PASSWORD"

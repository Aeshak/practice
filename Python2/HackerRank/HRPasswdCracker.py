# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

def findPass(d,originalLoginAttempt,words,left):
	if "".join(words) == originalLoginAttempt:
		return True
	if left != "":
		for i in d.keys():
			for j in d[i]:
				if left[0:len(j)] == j:
					words.append(j)
					left = left[len(j):]
					findPass(d,originalLoginAttempt,words,left)
	words = []
	left = originalLoginAttempt
	return False

t = int(raw_input().strip())
for _ in xrange(t):
	n = int(raw_input().strip())
	passn = raw_input().strip().split(' ')
	originalLoginAttempt = raw_input().strip()
	d = defaultdict(list)
	for _ in passn:
		d[_[0]].append(_)
	words = []
	if findPass(d,originalLoginAttempt,words,originalLoginAttempt):
		print " ".join(words)
	else:
		print "WRONG PASSWORD"


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
memo = set()

def findPass(left):
	global memo
	if left == "":
		return True
	char = left[0]
	if char in d.keys():
		for j in d[char]:
			if left[0:len(j)] == j:
				rest = left[len(j):]
				if rest not in memo:
					memo.add(rest)
					words.append(j)
					if findPass(rest):
						return True
					else:
						if len(words) != 0:
							words.pop()
	return False

t = int(raw_input().strip())
for _ in xrange(t):
	n = int(raw_input().strip())
	passn = raw_input().strip().split(' ')
	originalLoginAttempt = raw_input().strip()
	d = defaultdict(list)
	memo = set()
	for _ in passn:
		d[_[0]].append(_)
	words = []
	if findPass(originalLoginAttempt):
		print " ".join(words)
	else:
		print "WRONG PASSWORD"
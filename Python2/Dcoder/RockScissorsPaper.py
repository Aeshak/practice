def comp(i,j):
	if i == j:
		return 0
	if i == "P" and j == "R":
		return 1
	if i == "S" and j == "P":
		return 1
	if i == "R" and j == "S":
		return 1
	return -1
		
dummy = raw_input()
s = raw_input()
for i,j in zip(s[0::2],s[1::2]):
	if comp(i,j) > 0:
		print "Dcoder"
	elif comp(i,j) < 0:
		print "You"
	else:
		print "Draw"
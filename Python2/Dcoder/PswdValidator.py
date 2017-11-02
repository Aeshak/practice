def isValid(s):
	if len(s) < 6 or len(s) > 20:
		print "False"
		return
	# Find upper
	upper = 0
	lower = 0
	number = 0
	for i in s:
		if ord(i) >= 65 and ord(i) <= 90:
			upper = 1
		if ord(i) >= 97 and ord(i) <= 122:
			lower = 1
		if ord(i) >= 48 and ord(i) <= 57:
			number = 1
	if lower == upper == number == 1:
		print "True"
	else:
		print "False"
t = int(raw_input())
for i in range(t):
	s = raw_input()
	isValid(s)
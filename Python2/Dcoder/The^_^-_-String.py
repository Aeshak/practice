s = raw_input()
good = 0
bad = 0
for i in range(2,len(s)):
	sub = s[i-2:i+1]
	if sub == "^_^":
		good += 1
	if sub == "-_-":
		bad += 1
if good > bad:
	print "Cody is happy with Dcoder"
elif bad > good:
	print "Cody wants to leave job"
else:
	print "Cody doesn't know what to do"
str1 = raw_input()
str2 = raw_input()
if len(str1) != len(str2):
	print "No"
	exit()
count = 0
for i in str1:
	if i in str2:
		count += 1
if count != len(str1):
	print "No"
	exit()
print "Yes"
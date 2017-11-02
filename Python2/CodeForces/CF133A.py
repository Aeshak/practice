#python 2.7.6
p = raw_input()
flag = True
for i in p:
	if i == 'H' or i == 'Q' or i == '9':
		print "YES"
		flag = False
		break
if flag:
	print "NO"
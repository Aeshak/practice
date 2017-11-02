def validate(s):
	openType = [ '[', '(', '{']
	closeType = [ ']', ')', '}' ]
	stack = []
	for i in s:
		if i in openType:
			stack.append(i)
		if i in closeType:
			if stack == []:
				return 0
			c = stack.pop()
			if openType.index(c) != closeType.index(i):
				return 0
	if stack == []:
		return 1
	return 0

s = raw_input()
if validate(s) == 1:
	print("Yes")
else:
	print("No")
    
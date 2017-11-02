bstr = raw_input()
count = 0
for i in range(len(bstr)):
	if i != 0 and bstr[i] == bstr[i-1]:
		count+=1
		if count == 5:
			break
	else:
		count = 0
if count == 5:
	print("Bad")
else:
	print("Good")
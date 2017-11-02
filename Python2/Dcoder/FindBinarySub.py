s1,s2 = str(raw_input()).split(" ")
s1.lstrip('0')
s2.lstrip('0')
sIdx = 0
eIdx = len(s2)
found = 0
while eIdx <= len(s1):
	if s2 == s1[sIdx:eIdx]:
		found = 1
		break
	sIdx += 1
	eIdx += 1
if found == 1:
	print("1")
else:
	print("0")
def incC(char):
	if ord(char)>=97 and ord(char)<=122:
		return(chr(ord(char)-32))
	if ord(char)>=65 and ord(char)<=90:
		return(chr(ord(char)+32))
	return char
s = raw_input()
print("".join((map(incC,list(s)))))
    
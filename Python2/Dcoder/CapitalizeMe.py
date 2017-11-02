def incC(string):
	if ord(string[0])>=96 and ord(string[0])<=122:
		return(chr(ord(string[0])-32)+string[1:])
	return string
s = raw_input().strip().split(" ")
print(" ".join((map(incC,s))))
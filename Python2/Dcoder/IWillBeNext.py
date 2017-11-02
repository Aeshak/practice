def incC(ch):
	return(chr(ord(ch)+1))
s = raw_input()
print("".join((map(incC,s))))
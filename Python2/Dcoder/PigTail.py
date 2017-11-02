s = raw_input()
n = len(s)
consonants = ['a','e','i','o','u']
if str.lower(s[0]) in consonants:
	s += "w"
elif n>1:
	s = s[1:]+s[0]
	#t[0],t[n] = t[n],t[0]
	#s = "".join(t)
s+="ay"
print s
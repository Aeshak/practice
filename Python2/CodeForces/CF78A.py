vowels = "aeiou"
def count(s):
	c = 0
	for i in vowels:
		c += s.count(i)
	return c
p1 = raw_input()
p2 = raw_input()
p3 = raw_input()
c1 = count(p1)
c2 = count(p2)
c3 = count(p3)
if c1 == 5 and c2 == 7 and c3 == 5:
	print "YES"
else:
	print "NO"
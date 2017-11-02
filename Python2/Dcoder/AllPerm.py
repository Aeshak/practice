def perm(s,i,j,l):
	global ncomp
	ncomp +=1
	if i == len(s):
		return l
	if j == len(s):
		return l
	if i != j:
		t = list(s)
		t[i],t[j] = t[j],t[i]
		t = ''.join(t)
		if t not in l:
			l.append(t)
		else:
			return l
	l = perm(s,i+1,j,l)
	l = perm(s,i,j+1,l)
	return l
s = raw_input()
l = [s]
'''
for i in range(len(s)):
	for j in range(len(s)):
		l = perm(s,i,j,l)
print l
'''
ncomp = 0
l = perm(s,0,0,l)
print ncomp
for x in l:
	l = perm(x,0,0,l)
print len(l)
print ncomp
count = 0
for i in l:
	if int(i) > int(s):
		count += 1
print count
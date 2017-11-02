import string
t = int(raw_input())
count = 0
for i in range(t):
	s = raw_input()
	valid = True
	for j in range(len(s)):
		if s[j] == '_' or s[j] == '^':
			continue
		if j+1 == len(s) or j == 0:
			valid = False
			break
		if s[j-1] == '^' and s[j+1] == '^':
			continue
		valid = False
		break
	if valid:
		count += 1
print count

    

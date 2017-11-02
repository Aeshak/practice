a,b,s = map(int,raw_input().split())
st = abs(a)+abs(b)
if st == 0:
	print "Yes" if s%2 == 0 else "No"
elif s < st:
	print "No"
elif s == st:
	print "Yes"
else:
	print "Yes" if (s-st)%2 == 0 else "No"
    
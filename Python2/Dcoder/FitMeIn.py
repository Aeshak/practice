n,m = map(int,raw_input().split())
a,b = map(int,raw_input().split())
c,d = map(int,raw_input().split())
if a*b + c*d <= n*m:
	if a+c <= n and b <= m and d <= m:
		print "Yes"
		exit()
	if a+c <= m and b <= n and d <= n:
		print "Yes"
		exit()
	if b+d <= n and a <= m and c <= m:
		print "Yes"
		exit()
	if b+d <= m and a <= n and c <= n:
		print "Yes"
		exit()
	if a+d <= n and b <= m and c <= m:
		print "Yes"
		exit()
	if a+d <= m and b <= n and c <= n:
		print "Yes"
		exit()
	if b+c <= n and a <= m and d <= m:
		print "Yes"
		exit()
	if b+c <= m and a <= n and d <= n:
		print "Yes"
		exit()
print "No"

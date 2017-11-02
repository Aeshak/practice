import sys
def drawTri(s,n,A):
	if s <= 5:
		print " ".join(map(str,A))
		return
	out = ""
	for i in range(len(A)):
		tc = str(A[i])
		out += tc		
		if len(tc) == 2:
			out += " "
		elif len(tc) == 3:
			out += "  "
		else:
			out += "   "
	print out
def drawPyr(s,n,A, out):
	if n > s:
		return out
	"""
	if s == 10:
		sys.stdout.write("  "*(s-n))
	elif s > 5:
		sys.stdout.write("  "*(s-n))
	else:
		sys.stdout.write(" "*(s-n))
	drawTri(s,n,A)
	"""
	m = len(A)
	"""
	if s > 5 and m < 6:
		tp = '{:^12}'.format(" ".join(map(str,A)))
	else:
		tp = '{:^14}'.format(" ".join(map(str,A)))
	print(tp.rstrip())
	"""
	out += [A]
	B = [0]*m
	B[0] = A[0]
	for i in range(1,m):
		B[i] = A[i-1]+A[i]
	A = B + [1]
	return drawPyr(s,n+1,A,out)
s = int(raw_input())
A = [1]
out = []
out = drawPyr(s,1,A,out)
#sys.stdout.flush()
tf = "   ".join(map(str, out[-1]))
#print tf
n = len(tf)
if s%2 == 0:
	tf = tf[:n/2] + tf[(n/2)+2:]
	n -= 1
if s <= 5:
	n = 9
count = 0
for i in out:
	if s <= 5:
		tp = ("{:^"+str(n)+"}").format(" ".join(map(str,i)))
	else:
		if count == len(out)-1:
			tp = tf
		else:
			tp = ("{:^"+str(n)+"}").format("   ".join(map(str,i)))
	print(tp.rstrip())
	count += 1
#print len(" ".join(map(str, out[-1])))

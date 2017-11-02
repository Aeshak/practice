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
			out += "  "
		else:
			out += "   "
	print out
def drawPyr(s,n,A):
	if n > s:
		return
	if s > 5:
		sys.stdout.write("  "*(s-n))
	else:
		sys.stdout.write(" "*(s-n))
	drawTri(s,n,A)
	m = len(A)
	B = [0]*m
	B[0] = A[0]
	for i in range(1,m):
		B[i] = A[i-1]+A[i]
	A = B + [1]
	drawPyr(s,n+1,A)
n = int(raw_input())
A = [1]
drawPyr(n,1,A)
sys.stdout.flush()
    

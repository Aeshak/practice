def drawTri(s,n):
	if n > len(s):
		return
	print(s[0:n])
	drawTri(s,n+1)
def drawPyr(s,n):
	if n > s:
		return
	print(" "*((s-n)/2)+"*"*n)
	drawPyr(s,n+2)
#s = raw_input()
n = 9
drawPyr(n,1)
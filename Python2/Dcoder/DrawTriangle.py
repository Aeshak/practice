def drawTri(s,n):
	if n > len(s):
		return
	print(s[0:n])
	drawTri(s,n+1)
s = raw_input()
drawTri(s,1)
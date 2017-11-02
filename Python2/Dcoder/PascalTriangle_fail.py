import sys
def drawTri(n):
	ss = 0
	for i in range(n):
		if i == 0:
			sys.stdout.write("1")
			ss += 1
			continue
		ss += 1
		if i%2 == 0:
			sys.stdout.write(str(ss))
		else:
			sys.stdout.write("#")

def drawPyr(s,n):
	if n > s:
		return
	sys.stdout.write(" "*(s-n))
	drawTri(n)
	sys.stdout.write("\n")
	drawPyr(s,n+1)			

n = int(raw_input())
drawPyr(n,1)
sys.stdout.flush()
    
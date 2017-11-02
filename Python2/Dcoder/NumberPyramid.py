import sys
def drawTri(s,n):
	if n > len(s):
		return
	print(s[0:n])
	drawTri(s,n+1)

def downUp(n):
	if n <= 1:
		sys.stdout.write("1")
		return
	sys.stdout.write(str(n))
	downUp(n-1)
	sys.stdout.write(str(n))

def drawPyr(s,n):
	if n > s:
		return
	sys.stdout.write(" "*(s-n))
	downUp(n)
	sys.stdout.write("\n")
	drawPyr(s,n+1)

n = int(raw_input())
drawPyr(n,1)
sys.stdout.flush()

class Node:
	_size = 8
	def __init__(self,v):
		self.children = [None]*_size
		self.v = v
alls = 0
def explore(i,j,m,n):
	global alls
	alls += 1
	#print (i, j)
	#return
	if i < n-1:
		v = m[i+1][j]
		m[i+1][j] = 'X'
		if v == '1':
			explore(i+1,j,m,n)
	if i < n-1 and j < n-1 :
		v = m[i+1][j+1]
		m[i+1][j+1] = 'X'
		if v == '1':
			explore(i+1,j+1,m,n)
	if i < n-1 and j > 0:
		v = m[i+1][j-1]
		m[i+1][j-1] = 'X'
		if v == '1':
			explore(i+1,j-1,m,n)
	if j < n-1:
		v = m[i][j+1]
		m[i][j+1] = 'X'
		if v == '1':
			explore(i,j+1,m,n)
	if j > 0:
		m[i][j-1] = 'X'
		v = m[i][j-1]
		if v == '1':
			explore(i,j-1,m,n)
	if i > 0:
		m[i-1][j] = 'X'
		v = m[i-1][j]
		if v == '1':
			explore(i-1,j,m,n)
	if i > 0 and j < n-1:
		m[i-1][j+1] = 'X'
		v = m[i-1][j+1]
		if v == '1':
			explore(i-1,j+1,m,n)
	if i > 0 and j > 0:
		v = m[i-1][j-1]
		m[i-1][j-1] = 'X'
		if v == '1':
			explore(i-1,j-1,m,n)
	#return (i,j)
n = 6
s  = "100101\n"
s += "110001\n"
s += "100001\n"
s += "010000\n"
s += "110000\n"
s += "111000"
print s
m = [None]*6
s = s.split("\n")
for i in range(n):
	m[i] = list(s[i])
i = j = 0
count = 0
for i in range(n):
	for j in range(n):
		#res = None
		if m[i][j] == '1':
			explore(i,j,m,n)
			m[i][j] = '1'
			count += 1
	#print res
	#i += 1
	#j += 1
for l in m:
	print "".join(l)
print count
print alls
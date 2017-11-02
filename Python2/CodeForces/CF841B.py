dr = [0,0,-1,1]
dc = [1,-1,0,0]
def isValid(i,j,n,m):
	return i >= 0 and j >= 0 and i < n and j < m
	
def explore(i,j,n,m,a,v,c,ip,jp,res):
	for x in range(len(dr)):
		nn = i+dr[x]
		mm = j+dc[x]
		if nn == ip and mm == jp:
			continue
		if isValid(nn,mm,n,m) and v[nn][mm] != c and a[nn][mm] == 'A':
			v[nn][mm] = c
			print "%d,%d"%(nn,mm)
			if nn == ip and mm == jp:
				#print "HERE"
				res.append((nn,mm))
			explore(nn,mm,n,m,a,v,c,ip,jp,res)
	#print "i,j %d,%d"%(i,j)
	#return res

def cycleTest(i,j,n,m,a,v,c):
	res = list()
	explore(i,j,n,m,a,v,c,i,j,res)
	print res
	if len(res) != 0:
		return True
	return False

n = m = 5
#s = ["AAAAB","ABBAB","ABAAB","ABABB","AAAAA"]
s = ["AXXXB","ABBAB","ABAAB","AAABB","AAAAA"]
a = [None]*n
v = [None]*n
for i in range(n):
	a[i] = list(s[i])
	v[i] = [0]*m
c = 0
flag = 0
for i in range(n):
	for j in range(m):
		if a[i][j] == 'A':
			c += 1
			if cycleTest(i,j,n,m,a,v,c):
				print "Yes %d,%d,%d"%(i,j,c)
				flag = 1
				break
	if flag == 1:
		break


#explore(0,0,n,m,a,v,c,res)
#print res
for I in v:
	print I
    
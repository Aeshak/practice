#python 3.60
def seed(STEP,MOD):
	A = [0]*MOD
	y = 0
	for i in range(MOD):
		y = (y + STEP)%MOD
		A[y] += 1
	if 0 in A:
		return False
	return True
while True:
	try:
		STEP,MOD = map(int,input().strip().split())
	except:
		break
	if seed(STEP,MOD):
		print("%10d%10d    Good Choice"%(STEP,MOD))
	else:
		print("%10d%10d    Bad Choice"%(STEP,MOD))
	print()
g = map(int,raw_input().split(" "))
s = map(int,raw_input().split(" "))
sumg = sum(g)
sums = sum(s)
d = sumg-sums
if d > 0:
	print("Garry "+str(d))
elif d < 0:
	print("Sharry "+str(d*-1))
else:
	print("None 0")
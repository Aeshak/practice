import math
l,h,d = map(int,raw_input().split(" "))
maxLim = int(math.ceil(h/d))
count = 0
for i in range(1,maxLim+1):
	mult = i*d
	if mult>=l and mult<=h:
		count += 1
print(count)
    
n = int(raw_input())
A = map(int,raw_input().split())
k = A[0]
i = 0
count = 1
flag = -1
for i in range(1,n):
	if (flag == -1 or flag == 0) and A[i] > k:
		count += 1
		flag = 0
	elif (flag == -1 or flag == 1) and A[i] < k:
		count += 1
		flag = 1
	else:
		if flag == 0:
			flag = 1
			count += 1
		elif flag == 1:
			flag = 0
			count += 1
		else:
			break
	k = A[i]
#print count
if count == len(A):
	print "Yes"
else:
	print "No"
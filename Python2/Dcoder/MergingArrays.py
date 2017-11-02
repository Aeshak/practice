n1 = int(raw_input())
A = map(int,raw_input().split())
n2 = int(raw_input())
B = map(int,raw_input().split())
k = int(raw_input())
i = j = 0
n = n1+n2
for h in range(n):
	aends = False
	bends = False
	if i >= n1:
		aends = True
	if j >= n2:
		bends = True
	if bends or A[i] < B[j]:
		num = A[i]
		i += 1
	elif aends or A[i] >= B[j]:
		num = B[j]
		j += 1
	# print num
	if h+1 == k:
		print num
		break
    
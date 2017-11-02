m = 1000000007
n = int(raw_input())
A = map(int, raw_input().split())
answer = 1
for i in range(n):
	answer = ((answer%m)*(A[i]%m))%m
print answer
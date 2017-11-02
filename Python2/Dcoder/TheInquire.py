n = int(raw_input())
p = map(int,raw_input().split())
q = int(raw_input())
for i in range(q):
	a,b = map(int,raw_input().split())
	print sum(p[a-1:b])
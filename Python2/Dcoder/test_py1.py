def fact(n):
	if n == 0:
		return 1
	return n*fact(n-1)
#n = int(raw_input())
#print(fact(n))
s = raw_input()
res = ""
first = 0
for i in s[::-1]:
	if first == 0 and int(i) == 0:
		continue
	first = 1
	res+=i
print(res)
def gcd(a,b):
	if a==0 or b ==0:
		return 1
	if a==b:
		return a
	if a > b:
		return gcd(a-b,b)
	return gcd(a,b-a)

n = raw_input().split(".")
if len(n) <= 1:
	print("1")
	exit()
y = n[1].strip()
y = y.rstrip("0")
if y == "" or int(y) == 0:
	print("1")
	exit()
ly = "1"+"0"*len(y)
#s = int(ly)/int(y)
#print(int(ly)%int(y))
#if int(ly)%int(y) != 0:
s =int(ly)/gcd(int(ly),int(y))
print(s)
    
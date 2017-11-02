#Exponentia not sure why TC 3 fails
n = int(raw_input())
r = range(n+1) if n >=0 else range(n,1)[::-1]
A = list(map(lambda x: pow(2,x), r))
s = ",".join(map(str,A))
print(s)
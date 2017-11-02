n,a,b = map(int,raw_input().split())
h = range(a,n+1) + range(1, a)
print h[b%n] if b >= 0 else h[((-1*b)%n)*-1]

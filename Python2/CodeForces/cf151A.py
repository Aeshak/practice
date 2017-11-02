n, k, l, c, d, p, nl, np = map(int, raw_input().split())
p1 = (k*l)/nl
p2 = c*d
p3 = p/np
op = min(p1,p2,p3)/n
print op
n,r = map(int,raw_input().split())
count = 1
while (n*count-r)%10 != 0 and (n*count)%10 != 0:
   count += 1
print count

n = int(raw_input())
a,b = [0]*n,[0]*n
for i in range(n):
   a[i],b[i] = map(int,raw_input().split())
count = 0
for i in range(n):
   for j in range(n):
      if a[i] == b[j]:
         count+=1
print count

n = int(raw_input())
s = raw_input()
count = 0
for i in range(n):
   if i == n-1:
      break
   if s[i] == s[i+1]:
      count += 1
print count

n = int(raw_input())
A = map(int,raw_input().split())
crime = police = 0
for i in A:
   if i > 0:
      police += i
   else:
      if police != 0:
         police -= 1
      else:
         crime += 1
print crime 

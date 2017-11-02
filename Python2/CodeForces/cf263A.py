A = [[0]*5 for i in range(5)]
for i in range(5):
   c = 0
   for j in map(int,raw_input().split()):
      A[i][c] = j
      c += 1
for i in range(5):
   for j in range(5):
      if A[i][j] == 1:
         print(abs(2-i)+abs(2-j))
         break

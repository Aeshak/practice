# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

A = [5, 5, 104, 108, 112, 123, 291, 543, 934, 1221]
B = [5, 104, 111]
#print len(A)
#print len(B)
n1 = len(A)
n2 = len(B)
n = n1+n2
i = j = 0
for k in range(n):
   aends = False
   bends = False
   if i >= n1:
      aends = True
   if j >= n2:
      bends = True
   if bends or A[i] < B[j]:
      num = A[i]
      i += 1
   elif aends or A[i] >= B[j]:
      num = B[j]
      j += 1
   print num

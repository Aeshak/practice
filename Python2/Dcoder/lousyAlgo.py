import math
import sys

def isPrime(num,p):
	for i in p[:int(math.sqrt(num))]:
		if num % i == 0:
		 return 0
	return 1

def getPrime(n):
	counter = 0
	p = [2]
	num = 3
	while counter < n:
		if isPrime(num,p) == 1:
			p.append(num)
			counter += 1
		num += 1
	return p[counter-1]

t = int(raw_input())
nums = raw_input().split()
for i in range(t):
	n = int(nums[i])
	sys.stdout.write(str(getPrime(n)))
	if i != t-1:
		sys.stdout.write(" ")

#print(isPrime(23752356))

    
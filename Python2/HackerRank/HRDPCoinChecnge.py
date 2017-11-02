#!/bin/python

import sys

def make_change(coins, n):
	combinations = [0]*(n+1)
	combinations[0] = 1
	for coin in coins:
		for i in xrange(n+1):
			if i >= coin:
				combinations[i] += combinations[i-coin]
	return combinations[-1]

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
coins = map(int,raw_input().strip().split(' '))
print make_change(coins, n)

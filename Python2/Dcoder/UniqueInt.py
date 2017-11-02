n = int(raw_input())
A = map(int,raw_input().split())
num = reduce(lambda x,y: x^y, A)
print num
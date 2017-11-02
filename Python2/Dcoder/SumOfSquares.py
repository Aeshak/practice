a,b = map(int,raw_input().split(" "))
sqrs = map(lambda x: x**2, range(a,b+1))
print(sum(sqrs))
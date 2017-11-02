#python 2.7.6

x = raw_input()
a,b = x.split(" ")
a = int(a)
b = int(b)
if a+b == 6:
	print("Love")
elif abs(a-b) == 6:
	print("Love")
else:
	print("Hate")
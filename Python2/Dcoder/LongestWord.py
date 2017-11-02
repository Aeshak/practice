import string
words = raw_input().split()
m = 0
w = ""
for word in words:
	word = word.strip(string.punctuation)
	l = len(word)
	if l > m:
		w = word
		m = l
print w
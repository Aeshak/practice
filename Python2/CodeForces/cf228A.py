s = map(int,raw_input().split())
freq = dict.fromkeys(s, 0)
for i in range(len(s)):
   freq[s[i]] += 1
print 4-len(freq)
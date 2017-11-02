# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

out = ""
t = int(raw_input().strip())
for _ in xrange(t):
    n = int(raw_input().strip())
    passn = raw_input().strip().split(' ')
    loginAttempt = raw_input()
    for i in passn:
        loginAttempt = re.sub(i, " "+i+" ", loginAttempt)
    loginAttempt = re.sub("\s+", " ", loginAttempt).strip()
    flag = True
    for w in loginAttempt.split(" "):
        if w not in passn:
            out += "WRONG PASSWORD"
            flag = False
            break
    if flag:
        out += loginAttempt
    out += "\n"
print out.rstrip()
    
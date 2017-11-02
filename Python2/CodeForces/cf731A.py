# a 97 
## z 122
#from '97' to '122' (1 rotation counterclockwise),
#from '122' to '101' (5 clockwise rotations),
#from '101' to '117' (10 rotations counterclockwise),
#from '117' to '115' (2 counterclockwise rotations).
s = raw_input()
start = current = 0
end = 25
count = 0
for i in s:
   pos = ord(i)-97
   diff = abs(current-pos)
   count += min((26-diff), diff)
   current = pos
print count

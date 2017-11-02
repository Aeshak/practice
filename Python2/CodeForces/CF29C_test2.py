from collections import defaultdict

def addEdge(g,v,w):
	g[v].append(w)
	g[w].append(v)

n = input()

g = defaultdict(list)
for _ in xrange(n):
	a,b = raw_input().split()
	addEdge(g,a,b)
out = []
root = ''
for i in g.keys():
	if len(g[i]) == 1:
		root = i
		break
out.append(root)
p = root
while True:
	for i in g[p]:
		if i == out[-1]:
			continue
		if p != root:
			out.append(p)
		p = i
		break
	if len(g[p]) == 1:
		break
out.append(p)
print " ".join(out)
    
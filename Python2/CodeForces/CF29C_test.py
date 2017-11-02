import sys
sys.setrecursionlimit(1000000)
from collections import defaultdict
class Graph:
	def __init__(self,V):
		self.V = V
		self.g = defaultdict(list)
		self.visited = defaultdict(list)
	def addEdge(self,v,w):
		self.g[v].append(w)
		self.g[w].append(v)
		self.visited[v] = False
		self.visited[w] = False
		return (len(self.g[v]),len(self.g[w]))
	def traverse(self,V,out,parent= -1):
		if parent == -1:
			out.append(V)
			g.visited[V] = True
		for i in self.g[V]:
			if not self.visited[i]:
				self.visited[i] = True
				out.append(i)
				g.traverse(i,out,1)
		
n = int(raw_input())
g = Graph(n)
#count = sys.maxint
#maxcount = 0
V = ''
for _ in range(n):
	a,b = raw_input().split()
	num = g.addEdge(a,b)
out = []
for _ in g.g.keys():
	if len(g.g[_]) == 1:
		V = _
		break
#print V
g.traverse(V,out)
#out.append(V)
print " ".join(out)
   
import sys

class Node(object):
	def __init__(self, data, next):
		self.data = data
		self.next = next
class SingleList(object):
	head = None
	tail = None
	
	def append(self, data):
		node = Node(data, None)
		if self.head is None:
			self.head = self.tail = node
		else:
			self.tail.next = node
		self.tail = node

l = SingleList()
s = (raw_input()).split(" ")
for i in s:
	if int(i) == -1:
		break
	l.append(int(i))

node = l.head

def printRev(l, node):
	if node is None:
		return
	printRev(l,node.next)
	sys.stdout.write(str(node.data))
	if node is not l.head:
		sys.stdout.write(" ")
	

printRev(l,node)
sys.stdout.flush()
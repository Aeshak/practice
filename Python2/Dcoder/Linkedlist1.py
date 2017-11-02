class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node 
	def get_data(self):
		return self.data
	def get_next(self):
		return self.next_node
	def set_next(self, new_next):
		self.next_node = new_next

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head
		self.current = head
	def get_next(self):
		if self.current is None:
			return self.current.get_next()
		return None
	def insert(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			self.current = new_node
		else:			
			self.current.set_next(new_node)
		self.current = new_node
s = raw_input()
ll = LinkedList()
for i in s.split(" "):
	if int(i) == -1:
		break
	node = Node(i)
	#print(node.get_data())
	ll.insert(i)
node = ll.get_next()
#print(node.get_data())
while not (node is None):
	print(node.get_data())
	node = ll.get_next()
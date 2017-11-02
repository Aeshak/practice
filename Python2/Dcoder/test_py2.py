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
	def insert(self, data):
		new_node = Node(data)
		if head is None:
			self.head = new_node
		else:
			self.current.set_next(new_node)
		self.current = new_node
	def get_next(self):
		if self.current is not None:
			self.current = self.current.get_next()
		return self.current
		
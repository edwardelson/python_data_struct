#defining a stack with python's List
#LIFO Stack

class LIFO_Stack:
	def __init__(self):
		self.box = []

	def is_empty(self):
		return self.box == []

	def push(self, item):
		return self.box.append(item)

	def pop(self):
		return self.box.pop()

	def peek(self):
		return self.box[len(self.box)-1]

	def size(self):
		return len(self.box)

# other way of defining a LIFO Stack
class LIFO_Stack_2:
	def __init__(self):
		self.box = []

	def is_empty(self):
		return self.box == []

	def push(self, item):
		return self.box.insert(0, item)

	def pop(self):
		return self.box.pop(0)

	def peek(self):
		return self.box[0]

	def size(self):
		return len(self.box)
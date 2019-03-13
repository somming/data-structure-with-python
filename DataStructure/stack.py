class Stack:
	def __init__(self):
		self.container = list()


	def push(self,data):
		self.container.append(data)


	def pop(self):
		return self.container.pop()


	def empty(self):
		if not self.container:
			return True
		else:
			return False


	def peek(self):
		return self.container[-1]

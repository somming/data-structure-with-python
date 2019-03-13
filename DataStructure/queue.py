class Queue:
	def __init__(self):
		self.container = list()


	def push(self,data):
		self.container.append(data)


	def pop(self):
		return self.container.pop(0)


	def empty(self):
		if not self.container:
			return True
		else:
			return False


	def peek(self):
		return self.container[0]


if __name__ == "__main__":
	s = Queue()
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	s.push(5)

	while not s.empty():
		data = s.pop()
		print(data,end = ' ')
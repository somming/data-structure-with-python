# 스택 2개로 큐 하나를 구현한 MyQueue클래스를 구현하라
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


class MyQueue:
	def __init__(self):
		pushs = Stack()
		pops = Stack()
		self.container = [pushs,pops]


	def push(self,data):
		print("push : ",data)
		while not self.container[1].empty():
			temp = self.container[1].pop()
			self.container[0].push(temp)

		self.container[0].push(data)


	def pop(self):
		print("pop : ",self.peek())
		while not self.container[0].empty():
			temp = self.container[0].pop()
			self.container[1].push(temp)

		return self.container[1].pop()


	def empty(self):
		if self.container[0].empty() & self.container[1].empty():
			return True
		else:
			return False


	def peek(self):
		while not self.container[0].empty():
			temp = self.container[0].pop()
			self.container[1].push(temp)

		return self.container[1].peek()


if __name__ == "__main__":
	myqueue = MyQueue()

	myqueue.push(1)
	myqueue.push(2)
	myqueue.push(3)
	myqueue.push(4)
	myqueue.push(5)

	print(myqueue.container[0].container[0:])
	print(myqueue.container[1].container[0:])

	myqueue.pop()
	myqueue.pop()

	print(myqueue.container[0].container[0:])
	print(myqueue.container[1].container[0:])

	myqueue.push(6)
	myqueue.push(7)

	print(myqueue.container[0].container[0:])
	print(myqueue.container[1].container[0:])

	myqueue.pop()
	myqueue.pop()

	print(myqueue.container[0].container[0:])
	print(myqueue.container[1].container[0:])

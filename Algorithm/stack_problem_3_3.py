'''
접시 무더기 높이가 특정 수준 이상으로 높아지면 새로운 무더기를 만드는 자료구조 SetOfStacks를 구현

SetOfStacks는 여러 스택으로 구성되어야 하며, 이전 스택이 지정된 용량을 초과하는 경우

새로운 스택을 생성해야 한다. push()와 pop()은 스택이 하나인 경우와 동일하게 동작하도록 구현하시오
'''
class Stack:
	def __init__(self):
		self.container = list()
		self.max_size = 3
		self.size = 0


	def push(self,data):
		if self.isfull() :
			print("Stack is full")
			return

		self.container.append(data)
		self.size += 1


	def pop(self):
		self.size -= 1
		return self.container.pop()


	def empty(self):
		if not self.container:
			return True
		else:
			return False

	def isfull(self):
		if self.size == self.max_size:
			return True
		else:
			return False


	def peek(self):
		return self.container[-1]


class SetOfStacks:
	def __init__(self):
		self.container = [] #Stack이 담길 container
		self.container.append(Stack())
		self.stackcount = 1

	def push(self,data):
		if self.container[self.stackcount-1].isfull() : #현재 Stack이 꽉 찼다면!
			self.append_stack()

		self.container[self.stackcount-1].push(data)
		print("push : ",data)


	def pop(self):
		data = self.container[self.stackcount-1].pop()
		print("pop : ",data)
		if self.container[self.stackcount-1].empty() :
			self.container.pop()
			self.stackcount -= 1

		return data


	def append_stack(self):
		print("new Stack create")
		self.container.append(Stack())
		self.stackcount += 1


	def empty(self):
		pass

	def peek(self):
		pass


if __name__ == "__main__":
	stackset = SetOfStacks()
	stackset.push(1)
	stackset.push(2)
	stackset.push(3)
	stackset.push(4)
	stackset.pop()
	stackset.pop()
	stackset.pop()
	stackset.push(5)
	stackset.push(6)
	stackset.push(7)
	stackset.push(8)
	stackset.pop()
	stackset.pop()
	

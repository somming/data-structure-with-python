# push와 pop 두 가지 연산과 함께 최솟값을 반환하는 min을 갖춘 스택을 구현
# push, pop, min은 O(1)시간에 처리되도록 구현하시오

class Stack:
	def __init__(self):
		self.container = list()
		self.minnum = None #들어올때마다 최솟값을 비교하여 갱신


	def push(self,data):
		self.container.append(data)
		if not self.minnum:
			self.minnum = data
		elif data < self.minnum:
			self.minnum = data



	def pop(self):
		return self.container.pop()


	def empty(self):
		if not self.container:
			return True
		else:
			return False


	def min(self):
		return self.minnum


	def peek(self):
		return self.container[-1]


if __name__ == "__main__":
	s = Stack()
	s.push(7)
	s.push(5)
	s.push(3)
	s.push(4)
	s.push(2)

	m = s.min()
	print(m)

	while not s.empty():
		data = s.pop()
		print(data,end = ' ')

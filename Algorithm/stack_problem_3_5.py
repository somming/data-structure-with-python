import random
'''
스택 정렬 : 가장 작은 값이 위로 오도록 스택을 정렬하는 프로그램을 작성하라.
추가적으로 하나 정도의 스택은 사용해도 괜찮지만, 스택에 보관된 요소를 배열 등의 다른 자료구조로 복사할 수는 없다.
스택은 push, pop, peek, isEmpty 네 가지 연산을 제공해야 한다.
'''
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

def sort(unsorts):
	subs = Stack()
	count = len(unsorts.container)
	for i in range(count):
		temp = unsorts.pop()
		for j in range(count-i-1):
			if temp < unsorts.peek():
				subs.push(temp)
				temp = unsorts.pop()
			else:
				subs.push(unsorts.pop())

		unsorts.push(temp)
		while not subs.empty():
			unsorts.push(subs.pop())


if __name__ == "__main__":
	stack = Stack()
	for i in range(10):
		rnum = random.randrange(1,10)
		stack.push(rnum)

	print(stack.container[0:])

	sort(stack)

	print(stack.container[0:])


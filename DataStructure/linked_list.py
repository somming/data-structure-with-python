from random import randint

#노드, 데이터와 다음 노드를 가리킬 변수를 가진다.
class Node :
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

#LinkedList
class LinkedList:
	#초기화
	def __init__(self):
		self.head = None #LinkedList의 첫 노드
		self.tail = None #LinkedList의 마지막 노드

		self.current = None #현재 가리키는 노드
		self.before = None #현재 가리키는 노드의 전 노드

		self.num_of_data = 0 #노드의 갯수

	def __iter__(self):
		current = self.head
		while current:
			yield current
			current = current.next

	def __str__(self):
		values = [str(x) for x in self]
		return ' -> '.join(values)

	#노드 맨 뒤에 추가하는 함수 
	#새로운 노드를 만들고, 맨 뒤에 노드를 추가(현재 마지막 노드가 이것을 가리키게 한다.) 새로운 노드가 tail이 된다.
	#노드 갯수 1 증가 
	def append(self,data):
		new_node = Node(data)

		if self.head is None: #노드가 없다면
			self.head = self.tail = new_node
		
		else:
			self.tail.next = new_node
			self.tail = new_node

		self.num_of_data += 1

	#노드를 맨 처음에 추가하는 함수
	#새로운 노드를 만들고, 맨 앞에 노드를 추가(head가 된다.)
	def appendTofirst(self,data):
		new_node = Node(data)

		if self.head is None: #노드가 없다면
			self.head = self.tail = new_node

		else:
			self.head = new_node
			self.head.next = self.current.next

		self.num_of_data += 1

	#현재 가리키는 노드를 삭제하는 함수
	#만약 이것이 마지막노드였다면, 이전의 노드가 마지막 노드가 된다.
	#삭제될 노드의 전 노드가 삭제될 노드의 다음 노드를 가리키게 한다.
	#현재 가리키는 노드는 이전 노드가 된다.
	#노드 갯수 1 감소
	def delete(self):
		pop_data = self.current.data
		if self.current is self.tail:
			self.tail = self.before

		self.before.next = self.current.next;
		self.current = self.before

		self.num_of_data -= 1

		return pop_data

	def next(self):
		if self.current.next == None:
			return None
			
		self.before = self.current
		self.current = self.current.next

	def add_multiple(self, values):
		for v in values:
			self.append(v)

	def generate(self, n, min_value, max_value):
		self.head = self.tail = None
		for i in range(n):
			self.append(randint(min_value,max_value))
		return self
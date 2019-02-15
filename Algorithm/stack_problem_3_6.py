'''
동물 보호소 : 먼저 들어온 동물이 먼저 나가는 동물 보호소가 있다고 하자. 
이 보호소는 개와 고양이만 수용한다. 
사람들은 보호소에서 가장 오래된 동물부터 입양할 수 있는데, 개와 고양이 중 어떤 동물을 데려갈지 선택할 수 있다. 
하지만 특정한 동물을 지정해 데려갈 수는 없다. 이 시스템을 자료구조로 구현하라. 
이 자료구조는 enequeue, dequeueAny, dequeueDog, dequeueCat의 연산을 제공해야 한다.
'''
class Dog:
	count = 0
	def __init__(self):
		Dog.count += 1
		self.name = "Dog"+str(Dog.count)

class Cat:
	count = 0
	def __init__(self):
		Cat.count += 1
		self.name = "Cat"+str(Cat.count)

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


class AnimalShelter:
	def __init__(self):
		self.container = Queue()

	def enqueue(self,data):
		#print("in shelter : ",data.name)
		self.container.push(data)
		pass

	def dequeueAny(self):
		data = self.container.pop()
		print("out shelter : ",data.name)
		return data
		pass

	def dequeueDog(self):
		i=0
		while not isinstance(self.container.peek(),Dog) : #Dog가 나올 때까지
			data = self.container.pop()
			self.container.push(data)
			i+=1 # 몇 번 도는지 체크
			if i == len(self.container.container) :
				print("There is no Dog")
				return

		data = self.container.pop()
		print("out shelter : ",data.name)
		for j in range(len(self.container.container)-i) :
			data = self.container.pop()
			self.container.push(data)

		return data

	def dequeueCat(self):
		i=0
		
		while not isinstance(self.container.peek(),Cat) : #Cat가 나올 때까지
			data = self.container.pop()
			#print(data.name)
			self.container.push(data)
			i+=1 # 몇 번 도는지 체크
			if i == len(self.container.container) :
				print("There is no Cat")
				return

		data = self.container.pop()
		print("out shelter : ",data.name)
		for j in range(len(self.container.container)-i) :
			data = self.container.pop()
			self.container.push(data)

		return data


if __name__ == "__main__":
	queue = AnimalShelter()
	queue.enqueue(Dog())
	queue.enqueue(Dog())
	queue.enqueue(Cat())
	queue.enqueue(Dog())
	queue.enqueue(Cat())
	queue.enqueue(Dog())
	queue.enqueue(Dog())

	queue.dequeueCat()
	queue.dequeueCat()
	queue.dequeueCat()
	queue.dequeueAny()
	queue.dequeueDog()
	queue.dequeueAny()

#하나의 배열을 사용해 세 개의 스택을 구현
class Stack:
	container = list()
	stackcount=0
	stackap=0
	stackbp=0
	stackcp=0


	def __init__(self):
		self.stacknum = Stack.stackcount
		self.datacount = 0
		Stack.stackcount +=1
		if self.stacknum==0:
			Stack.stackap=0
		elif self.stacknum==1:
			Stack.stackbp=Stack.stackap
		else:
			Stack.stackcp=Stack.stackbp


	def push(self,data):
		self.datacount += 1
		if self.stacknum==0:
			self.container.insert(Stack.stackap,data)
			Stack.stackap+=1
			Stack.stackbp+=1
			Stack.stackcp+=1
			print("stackA data push : ",data)
			#print("stackAindex : ",Stack.stackap)
		elif self.stacknum==1:
			self.container.insert(Stack.stackbp,data)
			Stack.stackbp+=1
			Stack.stackcp+=1
			print("stackB data push : ",data)
			#print("stackBindex : ",Stack.stackbp)
		else:
			self.container.insert(Stack.stackcp,data)
			Stack.stackcp+=1
			print("stackC data push : ",data)
			#print("stackCindex : ",Stack.stackap)


	def pop(self):
		if self.stacknum==0:
			Stack.stackap-=1
			Stack.stackbp-=1
			Stack.stackcp-=1
			print("stackA data pop : ",self.peek())
			return self.container.pop(Stack.stackap)
			
		elif self.stacknum==1:
			Stack.stackbp-=1
			Stack.stackcp-=1
			print("stackB data pop : ",self.peek())
			return self.container.pop(Stack.stackbp)

		else:
			Stack.stackcp-=1
			print("stackC data pop : ",self.peek())
			return self.container.pop(Stack.stackcp)


	def empty(self):
		if not self.container:
			return True
		else:
			return False


	def peek(self):
		if self.stacknum==0:
			return self.container[Stack.stackap]
			
		elif self.stacknum==1:
			return self.container[Stack.stackbp]

		else:
			return self.container[Stack.stackcp]


if __name__ == "__main__":
	s1 = Stack()
	#print("s1 스택넘버 : ",s1.stacknum)
	s1.push(7)
	s1.push(5)
	s1.push(3)
	s1.push(4)
	s1.push(2)

	s2 = Stack()
	#print("s2 스택넘버 : ",s2.stacknum)
	s2.push(4)
	s2.push(3)
	s2.push(1)
	s2.push(3)
	s2.push(5)

	s3 = Stack()
	#print("s2 스택넘버 : ",s2.stacknum)
	s3.push(5)
	s3.push(9)
	s3.push(8)
	s3.push(7)
	s3.push(3)

	s1.pop()
	s2.pop()
	s3.pop()

	s2.push(1)
	s2.push(2)



print(Stack.container[0:])

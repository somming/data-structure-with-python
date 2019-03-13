#배열로 heap 구현하기
import math

class Node:
	def __init__(self):
		self.key = None

'''
힙은 큰 키에 자주 액세스 하거나 키 중심으로 정렬도니 시퀀스를 활용해야 할 때 유용한 자료구조이다.
힙은 최대 두 개의 자식 노드를 가지면서 마지막 레벨을 제외한 모든 레벨에서 노드들이 꽉 채워진 [완전 이진 트리]를 기본으로 한다.
각 노드의 값은 자신의 자식노드가 가진 값보다 크거나 같다.(최대 힙의 경우, 최소 힙은 반대)
'''
class Heap:
	def __init__(self):
		self.container = [None,] #원소들을 담을 배열
		self.heap_size = 0

	# 힙에 추가 시, 배열의 가장 마지막 레벨의 가장 왼쪽의 비어있는 공간에 들어가야 한다.
	# 부모노드와 비교해가며 위치를 바꿔간다.
	def insert(self,data):
		self.container.append(data)
		self.heap_size += 1
		cur = math.floor(self.heap_size/2)

		while cur != 0:
			self.heapify(cur)
			print(data,"삽입 : ",self.container)
			cur = math.floor(cur/2)


	def delete(self):
		deldata = self.container[1]
		self.container[1] = self.container.pop()
		self.heap_size -= 1

		self.heapify(1)

		print(deldata,"삭제 : ",self.container)


	#주어진 자료 구조에서 힙 성질을 만족하도록 하는 연산
	#자식 중 더 큰 값이 있다면 값을 교환하고 자식노드로 내려가서 재귀함수 호출 
	def heapify(self,index,size=None):
		cur = index
		left_index = 2*index
		right_index = 2*index+1

		if size == None:
			size = self.heap_size

		if left_index < size+1 and self.container[left_index] > self.container[cur]:
			cur = left_index

		if right_index < size+1 and self.container[right_index] > self.container[cur]:
			cur = right_index

		if cur != index :
			self.container[cur],self.container[index] = self.container[index],self.container[cur]
			self.heapify(cur,size)


	def build_heap(self,listh):
		#시간복잡도 O(nlogn)
		'''
		for i in range(1,len(lista)-1):
			self.insert(lista[i])
		'''

		#시간복잡도 O(n)
		self.container = listh
		self.heap_size = len(listh)-1
		
		level = math.floor(math.log(self.heap_size,2))-1
		cur = pow(2,level)

		print(level,cur)

		print(cur)
		while cur != 0:
			i = cur
			while i < pow(2,level+1): 
				print(i)
				self.heapify(i)
				i+=1
			cur = math.floor(cur/2)
			level -= 1
		

	def heapsort(self,listh):
		self.container = listh
		self.heap_size = len(listh)-1

		for i in range(self.heap_size // 2, 0, -1):
			self.heapify(i)

		print(self.container)

		for i in range(self.heap_size,0,-1):
			self.container[1],self.container[i] = self.container[i],self.container[1]
			#print("교환",self.container)
			self.heapify(1,i-1)
			#print("heapify :",self.container)

		print(self.container)



if __name__ =="__main__":
	lista = [None,2,7,8,9,5,1,3,4]
	heap = Heap()
	'''heap.insert(5)
	heap.insert(1)
	heap.insert(3)
	heap.insert(4)
	heap.insert(9)
	heap.insert(8)
	heap.insert(7)
	heap.insert(2)'''
	heap.heapsort(lista)


	print(heap.container)

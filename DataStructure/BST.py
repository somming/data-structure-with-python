from binary_tree import *

class BST:
	def __init__(self):
		self.root = None


	def get_root(self):
		return self.root


	def preorder_traverse(self,cur,func):
		if not cur:
			return

		func(cur.data)
		
		self.preorder_traverse(cur.left,func)

		self.preorder_traverse(cur.right,func)


	def insert(self,data):
		new_node = TreeNode()
		new_node.data = data

		cur = self.root

		if cur == None:
			self.root = new_node
			return

		while True:
			parent = cur
			if data < cur.data:
				cur = cur.left

				if not cur:
					parent.left = new_node
					return

			else:
				cur = cur.right
				if not cur:
					parent.right = new_node
					return


	def search(self,target):

			cur = self.root

			while cur:
				if target == cur.data:
					return cur

				elif target < cur.data:
					cur = cur.left


				elif target > cur.data:
					cur = cur.right

			return


	def remove(self, target):
		self.root,removed_node = self.__remove_recursion(self.root,target)
		removed_node.left = removed_node.right = None

		return removed_node


	def __remove_recursion(self, cur, target):
		if cur is None:
			return None, False

		elif target < cur.data:
			cur.left, rem_node = self.__remove_recursion(cur.left,target)

		elif target > cur.data:
			cur.right,rem_node = self.__remove_recursion(cur.right,target)

		else:
			#1. 리프 노드일 때
			if not cur.left and not cur.right:
				rem_node = cur
				cur = None

			#2-1. 자식 노드가 하나일 때: 왼쪽 자식이 있을 때
			elif not cur.right:
				rem_node = cur
				cur = cur.left

			#2-2. 자식 노드가 하나일 때, 오른쪽 자식이 있을 때
			elif not cur.left:
				rem_node = cur
				cur = cur.right

			#3. 자식 노드가 둘일 때
			else:
				#대체 노드를 찾는다.
				replace = cur.left
				while replace.right:
					replace = replace.right
				#삭제 노드와 대체 노드의 값을 교환한다.
				cur.data,replace.data = replace.data, cur.data
				#대체 노드를 삭제하면서 삭제된 노드를 받아온다.
				cur.left,rem_node = self.__remove_recursion(cur.left,replace.data)

		return cur,rem_node

		


if __name__ =="__main__":
	bst = BST()

	bst.insert(6)
	bst.insert(3)
	bst.insert(2)
	bst.insert(4)
	bst.insert(5)
	bst.insert(8)
	bst.insert(10)
	bst.insert(9)
	bst.insert(11)

	f = lambda x: print(x, end = ' ')

	bst.remove(9)

	bst.preorder_traverse(bst.get_root(),f)
	print()

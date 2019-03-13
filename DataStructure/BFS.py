class Node:
	def __init__(self,data):
		self.data = data
		self.childs = []


def bfs(v):
	queue = [] #queue를 사용
	visited = set()

	queue.append(v)

	while queue:
		node = queue.pop(0)
		if node in visited:
			continue
		print(node.data)
		visited.add(node)
		queue.extend(node.childs)

if __name__ =="__main__":
	A = Node(1)
	B = Node(2)
	C = Node(3)
	D = Node(4)
	E = Node(5)
	F = Node(6)

	A.childs = [B,E,F]
	B.childs = [D,E]
	C.childs = [B]
	D.childs = [C,E]

	bfs(A)
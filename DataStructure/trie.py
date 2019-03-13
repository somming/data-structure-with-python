class Node:
    def __init__(self, key, data=None):
        self.key = key #문자 하나
        self.data = data #마지막 글자라면 전체 단어 저장 아니라면 None
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur = self.head
        for char in string:
            if char not in cur.children:
                cur.children[char] = Node(char)
            cur = cur.children[char]
        cur.data = string

    def search(self, string):
        cur = self.head
        for char in string:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return False

        if(cur.data != None):
            return True

    def starts_with(self,prefix):
        cur = self.head
        result = []
        subtrie = None

        for char in prefix:
            if char in cur.children:
                cur = cur.children[char]
                subtrie = cur
            else:
                return False

        if subtrie.data is not None:
            result.append(subtrie.data)

        queue = list(subtrie.children.values())

        while queue:
            cur = queue.pop()
            if cur.data is not None:
                result.append(cur.data)

            queue += list(cur.children.values())

        return result

trie = Trie()

trie.insert("hello")
trie.insert("gone")
trie.insert("go")

print(trie.starts_with("go"))
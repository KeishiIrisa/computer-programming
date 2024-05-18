class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        if self.value in "+-*":
            return f"({self.left}{self.value}{self.right})"
        return str(self.value)

    def set_nodes(self, x, y):
        if not isinstance(x, Node) or not isinstance(y, Node):
            return NotImplemented

        self.left, self.right = x, y
        return self
    
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value and self.left == other.left and self.right == other.right
        return False

    def deepcopy(self):
        new_node = Node(self.value)
        if self.left is not None:
            new_node.left = self.left.deepcopy()
        if self.right is not None:
            new_node.right = self.right.deepcopy()
        return new_node

    def replace(self, c1, c2):
        if self.value == c1:
            self.value = c2
        if self.left is not None:
            self.left.replace(c1, c2)
        if self.right is not None:
            self.right.replace(c1, c2)
        return self


class BinaryTree():
    def __init__(self):
        self.root = None
    
    def search(self, key):
        return self._search_by_recursion(self.root, key)
    
    def _search_by_recursion(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self._search_by_recursion(node.left, key)
        else:
            return self._search_by_recursion(node.right, key)
        
    def insert(self, key, value):
        self.root = self._insert_by_recursion(self.root, key, value)
        return self
    
    def _insert_by_recursion(self, n, key, value):
        if n is None:
            return Node(key, value)
        if key < n.key:
            n.left = self._insert_by_recursion(n.left, key, value)
        else:
            n.right = self._insert_by_recursion(n.right, key, value)
        return n


exec(input())

class Node:
    def __init__(self, x):
        self.value = x
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


class Tree():
    def __init__(self, root_node):
        self.root = root_node
 
    def __str__(self):
        return str(self.root)
    
    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        else:
            return self._size(node.left) + 1 + self._size(node.right)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        else:
            left_height = self._height(node.left)
            right_height = self._height(node.right)
            return 1 + max(left_height, right_height)
    
    def parse_postorder_string(self, line):
        node_array = [Node(x) for x in line.split(" ")]
        stack = []
        for n in node_array:
            if n.value in "+-*":
                right, left = stack.pop(), stack.pop()
                stack.append(n.set_nodes(left, right))
            else:
                stack.append(n)
        self.root = stack.pop()
        return self
    
    def parse_inorder_string(self, line):
        node_array = [Node(x) for x in line.split(" ")]
        self.root = self.e(node_array)
        return self
    
    def f(self, node_array):
        if len(node_array) == 0:
            return None
        elif node_array[0].value in "1234567890":
            return node_array.pop(0)
        else:
            print("syntax error")
            return
    
    def t(self, node_array):
        n = self.f(node_array)
        if len(node_array) != 0 and node_array[0].value == "*":
            return node_array.pop(0).set_nodes(n, self.t(node_array))
        else:
            return n
    
    def e(self, node_array):
        n = self.t(node_array)
        if len(node_array) != 0 and node_array[0].value in "+-":
            return node_array.pop(0).set_nodes(n, self.e(node_array))
        else:
            return n
    
    def evaluate(self, node=None):
        if node is None:
            node = self.root

        if node.value.isdigit():
            return int(node.value)
        elif node.value == "+":
            return self.evaluate(node.left) + self.evaluate(node.right)
        elif node.value == "-":
            return self.evaluate(node.left) - self.evaluate(node.right)
        elif node.value == "*":
            return self.evaluate(node.left) * self.evaluate(node.right)
        elif node.value == "^":
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            if right < 0:
                return None
            return left ** right
    
    def count(self, k):
        return self._count(self.root, k)

    def _count(self, node, k):
        if node is None:
            return 0
        elif node.value == k and node.left is None and node.right is None:
            return 1
        else:
            return self._count(node.left, k) + self._count(node.right, k)

    def __eq__(self, other):
        if isinstance(other, Tree):
            return self.root == other.root
        return False


exec(input())

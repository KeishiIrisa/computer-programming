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


exec(input())
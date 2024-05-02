class Node:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

    def __str__(self):
        if self.value is None:
            return ""
        return self.value

    def set_nodes(self, x, y):
        if not isinstance(x, Node) or not isinstance(y, Node):
            return NotImplemented

        self.left, self.right = x, y
        return self


glb_count = []


def preorder(n):
    if n is None:
        return glb_count
    else:
        glb_count.append(0)
        preorder(n.left)
        preorder(n.right)


class Tree():
    def __init__(self, root_node):
        self.root = root_node
    
    def size(self):
        if self.root is None:
            return 0
        else:
            preorder(self.root)
            return len(glb_count)


exec(input())

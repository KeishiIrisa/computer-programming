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
glb_sequence_inorder = []


def preorder(n):
    if n is None:
        return glb_count
    else:
        glb_count.append(0)
        preorder(n.left)
        preorder(n.right)


def inorder(n, is_left):
    if n is None:
        return 
    elif is_left:
        inorder(n.left, True)
        glb_sequence_inorder.extend(["(", n.value])
        inorder(n.right, False)
    elif not is_left and n.value in ["+", "-", "*", "%"]:
        inorder(n.left, True)
        glb_sequence_inorder.append(n.value)
        inorder(n.right, False)
    else:
        glb_sequence_inorder.append(n.value)
        for i in range(glb_sequence_inorder.count("(")):
            glb_sequence_inorder.append(")")
        

class Tree():
    def __init__(self, root_node):
        self.root = root_node
 
    def  __str__(self):
        if self.root is None:
            return ""
        else:
            inorder(self.root, False)
            return "".join(glb_sequence_inorder)
    
    def size(self):
        if self.root is None:
            return 0
        else:
            preorder(self.root)
            return len(glb_count)

    def height(self):
        if self.root is None:
            return -1
        else:
            inorder(self.root, False)
            return glb_sequence_inorder.count(")")

exec(input())

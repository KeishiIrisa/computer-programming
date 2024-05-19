class Node:
    def __init__(self, key, value, height):
        self.key = key
        self.value = value
        self.height = height
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

    def search_between(self, s, t):
        return self._search_between_by_recursion(self.root, s, t, [])
    
    def _search_between_by_recursion(self, node, s, t, result):
        if node is None:
            return result
        if s <= node.key <= t:
            result.append({node.key: node.value})
        if node.key > s:
            self._search_between_by_recursion(node.left, s, t, result)
        if node.key < t:
            self._search_between_by_recursion(node.right, s, t, result)
        return result


class AVLTree(BinaryTree):
    def get_height(self, n):
        if n == None:
            return -1
        else:
            return n.height
    
    def is_AVL(self):
        if self.root == None:
            return True
        else:
            if -1 <= self.get_height(self.root.left) - self.get_height(self.root.right) <= 1:
                root_node_is_AVL = True
            else:
                root_node_is_AVL = False

            left_subtree, right_subtree = AVLTree(self.root.left), AVLTree(self.root.right)
            return root_node_is_AVL and left_subtree.is_AVL() and right_subtree.is_AVL()
    
    def _single_right_rotation(self, A):
        B = A.left
        A.left = B.right
        B.right = A
        A.height = 1 + max(self.get_height(A.left), self.get_height(A.right))
        B.height = 1 + max(self.get_height(B.left), self.get_height(B.right))
        return B
    
    def _single_left_rotation(self, A):
        B = A.right
        A.right = B.left
        B.left = A
        A.height = 1 + max(self.get_height(A.left), self.get_height(A.right))
        B.height = 1 + max(self.get_height(B.left), self.get_height(B.right))
        return B

    def _left_right_rotation(self, A):
        B = A.left
        C = A.left.right

        B.right = C.left
        C.left = A
        
        A.left = C.right
        C.right = A

        A.height = 1 + max(self.get_height(A.left), self.get_height(A.right))
        B.height = 1 + max(self.get_height(B.left), self.get_height(B.right))
        C.height = 1 + max(self.get_height(C.left), self.get_height(C.right))
        return C
    
    def _right_left_rotation(self, A):
        B = A.right
        C = A.right.left

        B.left = C.right
        C.right = B

        A.right = C.left
        C.left = A

        A.height = 1 + max(self.get_height(A.left), self.get_height(A.right))
        B.height = 1 + max(self.get_height(B.left), self.get_height(B.right))
        C.height = 1 + max(self.get_height(C.left), self.get_height(C.right))
        return C

    def insert(self, key, value):
        self.root = self._insert_by_recursion(self.root, key, value)
        return self
    
    def _insert_by_recursion(self, n, key, value):
        if n == None:
            return Node(key, value, 0)
        else:
            if key < n.key:
                n.left = self._insert_by_recursion(n.left, key, value)
            else:
                n.right = self._insert_by_recursion(n.right, key, value)
        
        n.height = 1 + max(self.get_height(n.left), self.get_height(n.right))

        h_left, h_right = self.get_height(n.left), self.get_height(n.right) 
        if h_left - h_right == 2:
            h_left_left, h_left_right = self.get_height(n.left.left), self.get_height(n.left.right) 
            if h_left_left - h_left_right == 1:
                n = self._single_right_rotation(n) 
            elif h_left_right - h_left_left == 1:
                n = self._left_right_rotation(n) 
        elif h_right - h_left == 2:
            h_right_left, h_right_right = self.get_height(n.right.left), self.get_height(n.right.right) 
            if h_right_right - h_right_left == 1:
                n = self._single_left_rotation(n) 
            elif h_right_left - h_right_right == 1:
                n = self._right_left_rotation(n)

        return n


if __name__ == "__main__":
    n = int(input())
    NewAVLTree = AVLTree()
    for i in range(n):
        line = input().split(" ")
        key, value = int(line[0]), line[1]
        NewAVLTree.insert(key, value)
        
    search_count = int(input())

    for i in range(search_count):
        key = int(input())
        if NewAVLTree.search(key) is not None:
            print(NewAVLTree.search(key).value)
        else:
            print("No record")

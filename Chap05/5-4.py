from bisect import insort


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


def print_multiple_tree_insert_between(n):
    NewBinaryTree = BinaryTree()
    for i in range(n+1):
        if i < n:
            line = input().split(" ")
            key, value = int(line[0]), line[1]
            NewBinaryTree.insert(key, value)
        else:
            line = input().split(",")
            range_min, range_max = int(line[0]), int(line[1])
            result = sorted(NewBinaryTree.search_between(range_min, range_max), key=lambda x: list(x.keys())[0])
            values_only = [list(item.values())[0] for item in result]
            print(values_only)


if __name__ == "__main__":
    n = int(input())
    print_multiple_tree_insert_between(n)

from abc import ABC, abstractmethod
import queue


class AbstractGraph:
    @abstractmethod
    def connnect(self, x, y):
        pass
    
    @abstractmethod
    def get_adjacent_nodes(self, x):
        pass
    
    def find_path_bfs(self, source, target):
        visited = [-1 for _ in range(self.num_nodes)]
        q = queue.Queue()
        q.put(source)
        visited[source] = source
        while not q.empty():
            u = q.get()
            for v in self.get_adjacent_nodes(u):
                if visited[v] == -1:
                    visited[v] = u
                    q.put()
        if visited[target] == -1:
            return
        
        path = []
        u = target
        while not u == source:
            path.append(u)
            u = visited[u]
        
        path.append(u)
        path.reverse()
        return path
    
    def find_cycle(self):
        for s in range(self.num_nodes):
            visited = [ False for _ in range(self.num_nodes)]
            if self.visit_and_detect_cycle(s, visited):
                return True
        return False

    def visit_and_detect_cycle(self, u, visited):
        has_cycle = False
        for v in self.get_adjacent_nodes(u):
            if visited[v]:
                return True
            else:
                visited[v] = True
                if self.visit_and_detect_cycle(v, visited):
                    has_cycle = True
                visited[v] = False
        return has_cycle
    
    def compute_indegrees(self):
        indegree = [0 for _ in range(self.num_nodes)]
        for i in range(self.num_nodes):
            for j in self.get_adjacent_nodes(i):
                indegree[j] += 1
        return indegree
    
    def topological_sort(self):
        sorted_index = []
        indegree = self.compute_indegrees()
        q = queue.Queue()
        for i in range(self.num_nodes):
            if indegree[i] == 0:
                q.put(i)
        while not q.empty():
            i = q.get()
            sorted_index.append(i)
            for j in self.get_adjacent_nodes(i):
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.put(j)
        return sorted_index
    
    
class DirectedGraphAdjacencyList(AbstractGraph):
    def __init__(self, n):
        self.num_nodes = n
        self.list = [ [] for _ in range(n)]
    
    def connect(self, x, y):
        if not y in self.list[x]:
            self.list[x].append(y)
    
    def get_adjacent_nodes(self, x):
        return self.list[x]


if __name__ == "__main__":
    num_nodes = int(input())
    g = DirectedGraphAdjacencyList(num_nodes)
    while True:
        line = input().strip().split(" ")
        if line[0] == "":
            break
        g.connect(int(line[0]), int(line[1]))
    if g.find_cycle():
        print("Topological sort impossible")
    else:
        print(" ".join(map(str, g.topological_sort())))

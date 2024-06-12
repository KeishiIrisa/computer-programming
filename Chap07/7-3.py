from abc import ABC, abstractmethod
import queue


class Edge:
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight

    def __str__(self):
        return "(" + str(self.to) + "," + str(self.weight) + ")"
    
    def __eq__(self, o):
        return self.to == o.to and self.weight == o.weight


class AbstractWeightedGraph:
    @abstractmethod
    def connect(self, x, y, weight):
        pass
    
    def get_adjacent_nodes(self, x):
        pass
    
    def dijkstra(self, s):
        d = [ float("inf") for i in range(self.num_nodes)]
        d[s] = 0.0
        visited = [ -1 for i in range(self.num_nodes)]
        visited[s] = s
        q = queue.PriorityQueue()
        q.put((d[s], s))
        while not q.empty():
            du, u = q.get()
            if d[u] == du:
                for e in self.get_adjacent_nodes(u):
                    v, w_uv = e.to, e.weight
                    if d[v] > d[u] + w_uv:
                        d[v] = d[u] + w_uv
                        visited[v] = u
                        q.put((d[v], v))
        return d, visited
    

class WeightedGraphAdjacencyList(AbstractWeightedGraph):
    def __init__(self, n):
        self.num_nodes = n
        self.list = [ [] for i in range(0, n)]

    def connect(self, u, v, w):
        e = Edge(v, w)
        if not e in self.list[u]:
            self.list[u].append(e)
    
    def get_adjacent_nodes(self, u):
        return self.list[u]
    

def compute_path(visited, source, target):
    path = []
    u = target
    while not u == source:
        path.append(u)
        u = visited[u]
    path.append(source)
    path.reverse()
    return path


if __name__ == "__main__":
    line = input().strip().split(" ")
    num_nodes, source = int(line[0]), int(line[1])
    g = WeightedGraphAdjacencyList(num_nodes)
    while True:
        line = input().strip().split(" ")
        if line[0] == "":
            break
        g.connect(int(line[0]), int(line[1]), float(line[2]))
    
    for i in range(num_nodes):
        d, _ = g.dijkstra(source)
        print(f"{i} {d[i]}")

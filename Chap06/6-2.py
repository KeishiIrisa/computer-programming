import queue


class Graph:
    def __init__(self, n):
        self.num_nodes = n
        self.adjacency_list = [[] for _ in range(n)]

    def connect(self, x, y):
        if not y in self.adjacency_list[x]:
            self.adjacency_list[x].append(y)
        if not x in self.adjacency_list[y]:
            self.adjacency_list[y].append(x)

    def visit_dfs(self, source):
        visited = [False for i in range(self.num_nodes)]
        self._visit_by_recursion(source, visited)
        return visited
    
    def _visit_by_recursion(self, i, visited):
        if visited[i] == True:
            return
        else:
            visited[i] == True
            for j in self.adjacency_list[i]:
                self._visit_by_recursion(j, visited)

    def visit_bfs(self, source):
        q = queue.Queue()
        q.put(source)
        visited = [(i==source) for i in range(self.num_nodes)]
        while not q.empty():
            u = q.get()
            for v in self.adjacency_list[u]:
                if visited[v] == False:
                    q.put(v)
                    visited[v] = True
        return visited
    
    def find_path_bfs(self, source, target):
        visited = [-1 for _ in range(self.num_nodes)]
        q = queue.Queue()
        q.put(source)
        visited[source] = source
        while not q.empty():
            u = q.get()
            for v in self.adjacency_list[u]:
                if visited[v] == -1:
                    visited[v] = u
                    q.put(v)
        path = []
        u = target
        while not u == source:
            if visited[u] == -1:
                return "No path"
            path.append(u)
            u = visited[u]
        path.append(source)
        path.reverse()
        return path
    

if __name__ == "__main__":
    graph_info = input().strip().split(" ")
    g = Graph(int(graph_info[0]))
    while True:
        string_list = input().strip().split(" ")
        if string_list[0] == '':
            break
        g.connect(int(string_list[0]), int(string_list[1]))
    
    path = g.find_path_bfs(int(graph_info[1]), int(graph_info[2]))
    if type(path) == str:
        print(path)
    else:
        print(" ".join(map(str, g.find_path_bfs(int(graph_info[1]), int(graph_info[2])))))

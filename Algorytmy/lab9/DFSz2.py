class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def dfs(self, start):
        visited = set()
        self._dfs_util(start, visited)

    def _dfs_util(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')

        if vertex in self.graph:
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    self._dfs_util(neighbor, visited)

g = Graph()

g.add_edge('A', 'B')
g.add_edge('A', 'F')
g.add_edge('B', 'C')
g.add_edge('B', 'E')
g.add_edge('C', 'D')
g.add_edge('D', 'B')
g.add_edge('D', 'H')
g.add_edge('E', 'D')
g.add_edge('E', 'G')
g.add_edge('G', 'F')
g.add_edge('F', 'G')
g.add_edge('F', 'E')
g.add_edge('H', 'G')


print("Przechodzenie DFS:")
g.dfs('A')


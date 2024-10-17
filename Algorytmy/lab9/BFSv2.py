from queue import Queue

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def bfs(self, start):
        visited = set()
        queue = Queue()
        queue.put(start)
        visited.add(start)

        while not queue.empty():
            vertex = queue.get()
            print(vertex, end=' ')

            if vertex in self.graph:
                for neighbor in sorted(self.graph[vertex], key=lambda x: (not x.isalnum(), x)):
                    if neighbor not in visited:
                        queue.put(neighbor)
                        visited.add(neighbor)

g = Graph()

g.add_edge('3', '7')
g.add_edge('3', '6')
g.add_edge('3', '2')
g.add_edge('7', '6')
g.add_edge('2', '6')
g.add_edge('2', '5')
g.add_edge('6', '5')
g.add_edge('5', '1')
g.add_edge('1', '0')
g.add_edge('0', '4')


print("Przechodzenie BFS:")
g.bfs('3')


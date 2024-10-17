import heapq

class Graph:
    def init(self):
        self.vertices = set()
        self.graph = {}

    def add_edge(self, u, v, w):
        self.vertices.add(u)
        self.vertices.add(v)
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def primMST(self):
        visited = {v: False for v in self.vertices}
        minHeap = []
        result = []
        start_vertex = next(iter(self.vertices))
        visited[start_vertex] = True

        for v, w in self.graph[start_vertex]:
            heapq.heappush(minHeap, (w, start_vertex, v))

        while minHeap:
            weight, u, v = heapq.heappop(minHeap)
            if visited[v]:
                continue

            visited[v] = True
            result.append((u, v, weight))

            for next_v, next_w in self.graph[v]:
                if not visited[next_v]:
                    heapq.heappush(minHeap, (next_w, v, next_v))

        return result

#Przykładowe użycie
g = Graph()
g.add_edge('A', 'B', 1)
g.add_edge('A', 'E', 4)
g.add_edge('A', 'F', 8)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'F', 6)
g.add_edge('B', 'G', 6)
g.add_edge('C', 'G', 2)
g.add_edge('C', 'D', 3)
g.add_edge('D', 'G', 1)
g.add_edge('D', 'H', 4)
g.add_edge('E', 'F', 5)
g.add_edge('F', 'G', 1)
g.add_edge('G', 'H', 1)

minimum_cost = 0
minimum_spanning_tree = g.primMST()
for u, v, weight in minimum_spanning_tree:
    minimum_cost += weight
    print(f"{u} {v}: {weight}")
print(f"Minimalne koszty = {minimum_cost}")
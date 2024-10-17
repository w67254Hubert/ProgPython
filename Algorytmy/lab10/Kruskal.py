class Graph:
    def __init__(self):
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def kruskal(self):
        T = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = {}

        for u, v, _ in self.graph:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v

        while e < len(parent) - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                T.append([u, v, w])
                parent[x] = y

        minCost = 0
        for u, v, weight in T:
            minCost += weight
            print(f"{u} -- {v} == {weight}")

        print(f"Minimalne koszty = {minCost}")


g = Graph()
g.add_edge('A','B', 1)
g.add_edge('A','E', 4)
g.add_edge('A','F', 8)
g.add_edge('B','F', 6)
g.add_edge('B','G', 6)
g.add_edge('B','C', 2)
g.add_edge('C','D', 3)
g.add_edge('C','G', 2)
g.add_edge('D','G', 1)
g.add_edge('D','H', 4)
g.add_edge('E','F', 5)
g.add_edge('F','G', 1)
g.add_edge('G','H', 1)

g.kruskal()
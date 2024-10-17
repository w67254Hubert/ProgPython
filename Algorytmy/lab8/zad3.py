import pandas
#bibliotegi z poradnika ogarnij
import networkx as nx
import matplotlib.pyplot as plt
#do dicsttrty
import sys

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}  # lista sąsiedztwa z wagami

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    

    def getAdjacencyMatrix(self):
        vertices = list(self.getVertices())
        numOfVertices = len(vertices)

        # tworzenie pustej macierzy
        adjacencyMatrix=[]
        adjacencylist = [0] * numOfVertices
        for x in range(numOfVertices):
            adjacencyMatrix.append(adjacencylist)
        
        # wypełnianie macierzy
        for vertex in self:
            vertexId = vertex.getId()
            connections = vertex.getConnections()
            for connection in connections:
                connectionId = connection.getId()
                weight = vertex.getWeight(connection)
                adjacencyMatrix[vertexId][connectionId] = weight

        return  adjacencyMatrix
    #pokazuje ogólną wizualizacje grafu bez wartości połączeń 
    def seeGraph(self):
        connectionList = []

        for vertex in self:
            vertexId = vertex.getId()
            connections = vertex.getConnections()
            for connection in connections:
                connectionId = connection.getId()
                connectionList.append([vertexId, connectionId])

        connections=[]
        for connection in connectionList:
            connections.append(connection)

        G = nx.Graph()
        G.add_edges_from(connections)
        nx.draw_networkx(G)
        plt.show()
    #algorytm Dijkstri działanie do rozkminienia / przerobienia   
    def dicstry(self,start):
        
        distances = {v: sys.maxsize for v in self.getVertices()}
        distances[start] = 0
        visited = set()

        while len(visited) < self.numVertices:
            current = None
            min_distance = sys.maxsize

            for vertex in self:
                if vertex.getId() not in visited and distances[vertex.getId()] < min_distance:
                    current = vertex
                    min_distance = distances[vertex.getId()]

            if current is None:
                break

            visited.add(current.getId())

            for neighbor in current.getConnections():
                weight = current.getWeight(neighbor)
                distance = distances[current.getId()] + weight

                if distance < distances[neighbor.getId()]:
                    distances[neighbor.getId()] = distance

        return distances




        
        


g = Graph()
# for i in range(6):
#     g.addVertex(i)
#     g.vertList


# g.addEdge(0, 1, 5)
# g.addEdge(0, 5, 2)
# g.addEdge(1, 2, 4)
# g.addEdge(2, 3, 9)
# g.addEdge(3, 4, 7)
# g.addEdge(3, 5, 3)
# g.addEdge(4, 0, 1)
# g.addEdge(5, 4, 8)
# g.addEdge(5, 2, 1)

# for v in g:
#     for w in v.getConnections():
#         print("( %s , %s )" % (v.getId(), w.getId()))


try:
    graf="2" #input("jaki chcesz graf?\n[1] nieskierowany\n[2] skierowany\n[3] ważony")
except ValueError:
    print("o nie to nie działa bo ktoś nie umie wykonać polecenia")

try:
    wiersz=3 #int(input('ile wieszhołków będzie?'))
except ValueError:
    print("o nie to nie działa bo ktoś nie umie wykonać polecenia")


for i in range(wiersz):
    g.addVertex(i)
    g.vertList

try:
    poł=3 #int(input('ile połączeń ma być?'))
except ValueError:
    print("o nie to nie działa bo ktoś nie umie wykonać polecenia")


if graf=="1":
    for i in range(poł):
        f=int(input('podaj początek połącznienia '+str(i)+":  "))
        t=int(input('podaj koniec połącznienia '+str(i)+":  "))
        g.addEdge(f, t,1)
        g.addEdge(t, f,1)

if graf=="2":
    for i in range(poł):
        f=int(input('podaj początek połącznienia '+str(i)+":  "))
        t=int(input('podaj koniec połącznienia '+str(i)+":  "))
        g.addEdge(f, t,1)
if graf=="3":
    for i in range(poł):
        f=int(input('podaj początek połącznienia '+str(i)+":  "))
        t=int(input('podaj koniec połącznienia '+str(i)+":  "))
        w=int(input('podaj wartość połącznienia '+str(i)+":  "))
        g.addEdge(f, t, w)


print()
# listę sąsiedztwa
print("lista sąsiectwa")
for i in g:
    print(i)


'\n'
print("macierz sąsiedztwa \n")
print(pandas.Series(g.getAdjacencyMatrix()))
lisForVis=g.getAdjacencyMatrix()

print('interpretacja graficzna grafu')
g.seeGraph()

#zadadanie 4

s = int(input('Podaj wieszchołek startowy\n s = '))
g.dicstry(s)
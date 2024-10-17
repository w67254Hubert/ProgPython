#  planarity nie chce sie zainstalować :l

# import planarity

# edgelist = [('a', 'b'), ('a', 'c'), ('a', 'd'), 
#  ('a', 'e'), ('b', 'c'),('b', 'd'),
#  ('b', 'e'), ('c', 'd'), ('c', 'e'), 
#  ('d', 'e')]
# print(planarity.is_planar(edgelist))
# edgelist.remove(('a','b'))
# print(planarity.is_planar(edgelist))
# print(planarity.ascii(edgelist))

# numOfVertices = 3
#         # print(graph,"co jest jako graf")
#         # Inicjalizacja macierzy
# # adjacencyMatrix = [[0] * numOfVertices for _ in range(numOfVertices)]
# adjacencyMatrix=[]
# adjacencylist = [0] * numOfVertices

# for x in range(numOfVertices):
#     adjacencyMatrix.append(adjacencylist)

# # adjacencyMatrix=[ [0] for _ in range(numOfVertices)]
# print(adjacencyMatrix)


# First networkx library is imported 
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt
   
  
# Defining a Class
class GraphVisualization:
   
    def __init__(self):
          
        # visual is a list which stores all 
        # the set of edges that constitutes a
        # graph
        self.visual = []
          
    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)
          
    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        print(self.visual)
        nx.draw_networkx(G)
        plt.show()
  
# Driver code
G = GraphVisualization()
G.addEdge(0, 2)
G.addEdge(1, 2)
G.addEdge(1, 3)
G.addEdge(5, 3)
G.addEdge(3, 4)
G.addEdge(1, 0)
G.visualize()




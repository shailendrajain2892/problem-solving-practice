from collections import defaultdict
class Graph:
    def __init__(self, vertices, edges) -> None:
        self.vertices = vertices
        self.matrix = [[0]*vertices for _ in range(vertices)]
        self.edges = edges
        self.adjacencyList = defaultdict(list)
        self.create_adjacency_matrix()
        self.createAdjacencyList()

    def create_adjacency_matrix(self) -> None:
        for edge in self.edges:
            u, v, w = edge
            self.matrix[u][v] = w
            self.matrix[v][u] = w
    
    def addEdge(self, u, v, w) -> None:
        if u>0 and u<len(self.matrix[0]) and v > 0 and v<len(self.matrix):
            self.matrix[u][v] = w
            self.matrix[v][u] = w
            
    def createAdjacencyList(self) -> None:
        for edge in self.edges:
            u, v, w = edge
            self.adjacencyList[u].append(v)
            self.adjacencyList[v].append(u)
        
    def printAdjacencyList(self) -> None:
        # Print the adjacency list
        for vertex, neighbors in self.adjacencyList.items():
            print(f"{vertex}: {neighbors}")

undirectied_graph = Graph(4, [(0, 1, 2),(0,2, 4), (1, 2, -5), (2,3, 1)])
print(undirectied_graph.matrix)
undirectied_graph.printAdjacencyList()

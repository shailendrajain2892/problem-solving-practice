from collections import defaultdict
from queue import Queue
class Graph:
    def __init__(self, edges) -> None:
        self.adj_list = defaultdict(list)
        self.visited = set()
        for edge in edges:
            u, v = edge
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
    
    def printList(self) -> None:
        for vertex, adjnodes in self.adj_list.items():
            print(f"{vertex}:{adjnodes}")

    # undirected graph
    def BFS(self, source, visited, res):
        q = Queue()
        q.put(source)
        visited.add(source)
        while not q.empty():
            current_vertex = q.get()
            if current_vertex is not None:
                res.append(current_vertex)
            
            for neighbor in self.adj_list.get(current_vertex):
                if neighbor not in visited:
                    q.put(neighbor)
                    visited.add(neighbor)
        return res
    
    def bfs_disconnected(self):
        disconnectedGraphBFS = []
        disconnectedComponent=0
        for node in self.adj_list:
            if node not in self.visited:
                self.BFS(node, self.visited, disconnectedGraphBFS)
                disconnectedComponent+=1
        return disconnectedGraphBFS, disconnectedComponent


und_graph = Graph([(0,None), (1, 3), (2, 4), (4, 5)])
# und_graph.printList()
print(und_graph.bfs_disconnected())
# print(und_graph.BFS(0))
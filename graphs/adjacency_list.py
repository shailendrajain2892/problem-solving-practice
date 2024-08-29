from collections import defaultdict
class Graph:
    def __init__(self, edges) -> None:
        self.adj_list = defaultdict(list)
        for edge in edges:
            u, v = edge
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
    
    def printList(self) -> None:
        for vertex, adjnodes in self.adj_list.items():
            print(f"{vertex}:{adjnodes}")
    
ug = Graph([[0, 1], [0, 2], [1, 2], [2,3]])
ug.printList()
from queue import Queue
from collections import defaultdict

def BFS(graph, start_node, source, vistied, source_node):
    print(f"Running for source : {source}")
    q = Queue()
    q.put(start_node)
    vistied.add(start_node)
    source_node[start_node] = source

    while not q.empty():
        current_node = q.get()
        for adj_node in graph[current_node]:
            if adj_node not in vistied:
                vistied.add(adj_node)
                source_node[adj_node] = source
                q.put(adj_node)
            elif source_node.get(adj_node) == source:
                print(f"Cycle detected at node : {adj_node}")
                return True
    
    return False
            
def detect_cycle(graph):
    visited = set()
    source_node = defaultdict()
    for node in graph:
        if node not in visited:
            if BFS(graph, node, node, visited, source_node):
                return True
    return False

graph = {
    0: [1],
    1: [],
    2: [1, 3], 
    3: [4],
    4: [5],
    5: [3]
}
print(f"Cycle in a give Graph : {detect_cycle(graph)}")
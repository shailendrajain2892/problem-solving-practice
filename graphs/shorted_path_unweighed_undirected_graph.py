from queue import Queue
from collections import defaultdict
def shortest_path_unweighed_undirected_graph(graph, source, shortest_path=defaultdict()):
    queue = Queue()
    visited = set()
    distance = 0

    queue.put((source, distance))
    visited.add(source)

    while not queue.empty():
        node, distance = queue.get()
        shortest_path[node] = distance
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put((neighbor, distance+1))

    return shortest_path
graph = {
    0: [1,2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [4, 2, 6],
    6: [5]
}

print(shortest_path_unweighed_undirected_graph(graph, 0))
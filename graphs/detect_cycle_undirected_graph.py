from collections import defaultdict
from queue import Queue

def bfs(graph, source, visited, parent=defaultdict()):
    q = Queue()
    q.put(source)
    visited.add(source)
    parent[source] = -1

    while not q.empty():
        current_node = q.get()
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current_node
                q.put(neighbor)
            elif parent[current_node] != neighbor:
                return True
    return False


def dfs(graph, source, visited, parent):
    visited.add(source)
    for neighbor in graph[source]:
        if neighbor not in visited:
            visited.add(neighbor)
            return dfs(graph, neighbor, visited, source)
        elif neighbor != parent:
            return True
    return False

# DFS & BFS based solution
def detect_cycle(graph, source):
    visited = set()
    parent = -1
    # return dfs(graph, source, visited, parent)
    return bfs(graph, 0, visited)

graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 4],
    3: [0, 4], 
    4: [2, 3]
}
#     0
#    / \
#   1   3
#   \     /
#    2   /
#    \  /
#     4
print(f"Graph has cycle : {detect_cycle(graph, 0)}")
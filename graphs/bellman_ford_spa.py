from collections import defaultdict

def bellman_ford_spa(graph, source):
    dist = {vertex:float('inf') for vertex in graph}

    dist[source] = 0

    for _ in range(len(graph)-1):
        for u in graph:
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    
    for u in graph:
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                return "Graph has negative wait cycle"

    return dist

edges = [('A', 'B', 2), ('B', 'C', 3), ('C', 'D', 6), ('D', 'B', 4)]
def create_graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        u, v, w = edge
        graph[u].append((v, w))
        graph[v].append((u, w))
    return graph
graph = create_graph(edges)
print(bellman_ford_spa(graph, 'A'))


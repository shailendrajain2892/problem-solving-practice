import heapq
def dijkstras_spa(graph, source):

    dist = {node:float('inf') for node in graph}
    dist[source] = 0

    minHeap = []
    heapq.heappush(minHeap, (dist[source], source))


    while minHeap:
        weight, node = heapq.heappop(minHeap)
        for adj_node, adj_node_weight in graph[node]:
            if adj_node_weight + weight < dist[adj_node]:
                dist[adj_node] = adj_node_weight + weight
                heapq.heappush(minHeap, (dist[adj_node], adj_node))
    
    return dist

graph = { # node, weight
    0: [(1, 5), (3, 4), (2, 2)],
    1: [(0, 5), (3, 1)],
    2: [(0, 2), (3, 1)],
    3: [(1, 1), (0, 4), (2, 1)]
}
print(dijkstras_spa(graph, 0))
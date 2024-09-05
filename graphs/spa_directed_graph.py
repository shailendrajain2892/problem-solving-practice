from collections import defaultdict, deque
    
def topological_sort(graph):
    indegree = {node: 0 for node in graph}
    
    for node in graph:
        for adj_node_w in graph[node]:
            if adj_node_w:
                adj_node, _ = adj_node_w
                indegree[adj_node] += 1
    
    queue = deque([node for node, degree in indegree.items() if degree == 0])

    topological_order = []
    while queue:
        current_node = queue.popleft()
        topological_order.append(current_node)
        for adj_node_w in graph[current_node]:
            if adj_node_w:
                adj_node, _ = adj_node_w
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)
    
    if len(topological_order) == len(graph):
        return topological_order
    else:
        return f"Graph has a cycle, topological sort is not possible : {topological_order}"

def spa(graph, source):
    # create a distance array and assign infinite value to each node
    distance = defaultdict()
    for node in graph:
        distance[node] = float('inf')
    
    sorted_list = topological_sort(graph)
    print(sorted_list)
    distance[source] = 0
    for vertex in sorted_list:
        for adj_node_w in graph[vertex]:
            if adj_node_w:
                adj_node, weight = adj_node_w
                if weight + distance[vertex] < distance[adj_node]:
                    distance[adj_node] = weight + distance[vertex] 
    
    return distance

graph = {
    0: [(1, 2), (4, 1)],
    1: [(2, 3)],
    2: [(3, 6)],
    3: [()],
    4: [(2, 2), (5, 4)],
    5: [(3, 1)]
}
print(spa(graph, 0))
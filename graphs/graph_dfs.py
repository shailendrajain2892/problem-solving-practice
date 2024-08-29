def dfs_disconnected(graph):
    visited = set()
    dfs_path = []
    for node in graph:
        if node not in visited:
            graph_dfs(graph, node, dfs_path, visited)
    return dfs_path

def graph_dfs(graph, source, dfs_list, visited):
    
    if visited is None:
        visited = set()
    
    if dfs_list is None:
        dfs_list = []

    visited.add(source)
    dfs_list.append(source)

    for neighbor in graph[source]:
        if neighbor not in visited:
            graph_dfs(graph, neighbor, dfs_list, visited)



# graph = {
#     1: [2, 3],
#     2: [4],
#     3: [5],
#     4: [],
#     5: []
# }
graph = {
    1: [2, 3],
    2: [],
    3: [],
    4: [5, 6],
    5: [],
    6: []
}

dfs_graph_path = dfs_disconnected(graph)
# graph_dfs(graph, 1, dfs_graph_path)
# dfs_disconnected(graph)
print(dfs_graph_path)
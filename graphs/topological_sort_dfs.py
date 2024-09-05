def dfs(graph, node, visited, stack):
    visited.add(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack)
    
    stack.append(node)

def topological_sort(graph):
    visited = set()
    stack = []
    
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited, stack)
    

    # Print in topological order by reversing the stack order
    while stack:
        print(stack.pop(), end=" ")

graph = {
    4: [0, 1],
    5: [0],
    3: [1],
    2: [3],
    1: [],
    0: []
}

topological_sort(graph)
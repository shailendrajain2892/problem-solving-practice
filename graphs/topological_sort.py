from collections import defaultdict
from queue import Queue

def topological_sort(graph):
    sorted_list = []

    # crate queue to store nodes
    queue = Queue()

    
    #calculate indegree for every node 
    indegree = defaultdict()
    for node, adj_nodes in graph.items():
        if node not in indegree:
            indegree[node] = 0
        for adj_node in adj_nodes:
            indegree[adj_node]=indegree.get(adj_node, 0)+1
    
    # put all the nodes into queue whose indegreee is 0 
    for node, degree in indegree.items():
        if degree == 0:
            queue.put(node)

    # now process the nodes in the queue using BFS
    while not queue.empty():
        current_node = queue.get()
        sorted_list.append(current_node)
        for adj_node in graph[current_node]:
            indegree[adj_node]-=1
            if indegree[adj_node] == 0:
                queue.put(adj_node)
    
    return sorted_list

graph = {
    0: [2, 3],
    1: [3, 4],
    2: [3],
    3: [],
    4: []
}
print(topological_sort(graph))
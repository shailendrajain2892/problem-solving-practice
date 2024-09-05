from collections import defaultdict
from queue import Queue


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = { course: [] for course in range(numCourses)}
        res = []
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])

        indegree = {node:0 for node in graph}
        for node, adj_nodes in graph.items():
            for adj_node in adj_nodes:
                indegree[adj_node] += 1
        
        q = Queue()

        for node, degree in indegree.items():
            if degree == 0:
                q.put(node)

        while not q.empty():
            node = q.get()

            res.append(node)
            for adj_node in graph[node]:
                indegree[adj_node]-=1
                if indegree[adj_node] == 0:
                    q.put(adj_node)
        return res
            
print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
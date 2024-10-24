from math import sqrt
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap=[]
        for point in points:
            x, y = point
            dist_sqr_sm = (x**2) + (y**2)
            heapq.heappush(max_heap, [-1*dist_sqr_sm, point])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [distance_point[1] for distance_point in max_heap]
    
points = [[0,2],[2,0],[2,2]]
k = 2
print(Solution().kClosest(points, k))

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-1*stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            y, x = heapq.heappop(max_heap), heapq.heappop(max_heap)
            y , x = -1*y, -1*x
            diff = abs(y-x)
            if diff != 0 :
                heapq.heappush(max_heap, -1*diff) 
        return -1*max_heap[0]

print(Solution().lastStoneWeight([1,2]))
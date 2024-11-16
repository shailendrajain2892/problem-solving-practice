import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []

        for i in range(k):
            heapq.heappush(maxHeap, [-nums[i], i])
        
        res = []
        res.append(-1*maxHeap[0][0])
        for i in range(k, len(nums)):
            heapq.heappush(maxHeap, [-1*nums[i], i])

            while maxHeap[0][1] <= i-k:
                heapq.heappop(maxHeap)
            
            res.append(-maxHeap[0][0])
            
            
            
        return res
nums = [1,2,1,0,4,2,6]
k = 3
print(Solution().maxSlidingWindow(nums, k))
        
import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        h = []
        
        for i in range(k):  
            heapq.heappush(h, nums[i])
        
        for i in range(k, len(nums)):
            heapq.heappush(h, nums[i])

        return heapq.heappop(h)
    
print(Solution().findKthLargest([3,2,1,5,6,4], 2))
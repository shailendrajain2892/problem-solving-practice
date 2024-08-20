import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        numsMap = {}
        h = []
        result = []
        # create number map to count freq
        for n in nums:
            numsMap[n] = 1+numsMap.get(n, 0)
        
        # populate heap with default value of k size
        for _ in range(k):
            heapq.heappush(h, (0,0))
        
        # iterate through dict and push and pop to heap
        for num, freq in numsMap.items():
            heapq.heappushpop(h, (freq, num))
        
        # iterate throuh heap and return result
        for r in h:
            result.append(r[1])
        return result
    
print(Solution().topKFrequent([1,2], 2))
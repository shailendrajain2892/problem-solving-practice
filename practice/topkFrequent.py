from collections import Counter
import heapq
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        res = []
        freqMap = [[] for i in range(len(nums)+1)]

        for num, freq in counter.items():
            freqMap[freq].append(num)
        
        for i in range(len(freqMap)-1, -1, -1):
            for n in freqMap[i]:
                res.append(n)
                if len(res) == k:
                    return res
        # minHeap = []
        # for k, v in counter.items():
        #     heapq.heappush(minHeap, (v, k))
        #     if len(minHeap) > k:
        #         heapq.heappop(minHeap)
        # return [k for v, k in minHeap]

nums = [1, 1,  2, 2, 3, 3, 3]
print(Solution().topKFrequent([7, 7], 1))

# TC = O(klogn)
# SC = O(k)
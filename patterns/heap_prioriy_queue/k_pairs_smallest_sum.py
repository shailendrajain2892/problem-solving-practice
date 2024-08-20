import heapq
class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        heap=[]
        result=[]

        for n1 in nums1:
            for n2 in nums2:
                if len(heap)<k:
                   heapq.heappush(heap, (-(n1+n2), [n1,n2]))
                else:
                    heapq.heappushpop(heap, (-(n1+n2), [n1,n2]))

        return [h[1] for h in heap]
    
print(Solution().kSmallestPairs([1,7,11], [2,4,6], 3))
from typing import List
from collections import deque
# Monotonically decreasing queue 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        l = 0
        for r, n in enumerate(nums):
            while q and n > q[-1]:
                q.pop()
            q.append(n)
            if r >= k and nums[r-k]==q[0]:
                q.popleft()
            if r-l+1 == k:
                output.append(q[0])
                l+=1
        return output

nums = [1, 1, 1, 1, 1, 4, 5]
nums2 = [8, 7, 6, 9]
num3 = [1,2,1,0,4,2,6]
nums4 = [1, -1]
nums5 = [7, 2, 4]
k = 2
print(Solution().maxSlidingWindow(nums5, k))
        

        
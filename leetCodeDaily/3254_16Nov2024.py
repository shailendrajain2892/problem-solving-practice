from typing import List


class Solution:
    def areConsecutive(self, nums):
        if not nums:
            return False
        min_num, max_num = min(nums), max(nums)
        return len(nums) == max_num-min_num+1 and len(set(nums)) == len(nums)

    def areSorted(self, nums):
        for idx in range(1, len(nums)):
            if nums[idx] != nums[idx-1]+1:
                return False
        return True

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        window, res, resIdx = [], [-1]*(len(nums)+1-k), 0
        for idx, n in enumerate(nums):
            window.append(n)
            if len(window) > k:
                window.remove(window[0])
                resIdx+=1
            if len(window) == k and self.areConsecutive(window) and self.areSorted(window):
                res[resIdx] = max(window)
            
        return res

nums = [1,2,3,4,3,2,5]
print(Solution().resultsArray(nums, 3))
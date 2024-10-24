from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset= []
        nums.sort()
        def dfs(i):    
            if i == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1)
        dfs(i=0)
        return res

print(Solution().subsets([1,2,1]))

        

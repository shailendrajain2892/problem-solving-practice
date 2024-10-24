from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, subset, total):
            if total == target:
                res.append(subset[::])
                return
            if total > target or i >= len(candidates):
                return
            
            subset.append(candidates[i])
            dfs(i+1, subset, total+candidates[i])

            subset.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, subset, total)
        dfs(0, [], 0)
        return res

print(Solution().combinationSum([9,2,2,4,6,1,5], 8))
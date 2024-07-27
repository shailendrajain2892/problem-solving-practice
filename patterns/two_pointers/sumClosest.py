class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        r = float('inf')
        minDiff= float('inf')
        nums.sort()
        for i in range(len(nums)-1):
            j, k = i+1, len(nums)-1
            while j<k:
                sm = nums[i]+nums[j]+nums[k]
                if sm==target:
                    r=sm
                    return r
                elif sm<target:
                    diff = target-sm
                    j+=1
                else:
                    diff = sm-target
                    k-=1
                if diff < minDiff:
                    r = sm
                    minDiff = diff
        return r if r != float('inf') else 0 # type: ignore

print(Solution().threeSumClosest([-1,-1,-1,-1,-1], 5))
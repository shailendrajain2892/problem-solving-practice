class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]  
        target=0
        nums.sort()
        for idx, a in enumerate(nums):
            if idx>0 and a == nums[idx-1]:
                continue
            l=idx+1
            r=len(nums)-1
            while l < r:
                threeSum = a+nums[l]+nums[r]
                if threeSum == target:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                elif threeSum > 0:
                    r-=1
                else:
                    l+=1
        return res

print(Solution().threeSum(nums=[-1,0,1,2,-1,-4]))
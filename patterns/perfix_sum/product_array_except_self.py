class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix=[1]*n
        suffix=1
        res = [1]*n
        # calculate prefix
        for i in range(1, n):
            res[i]  = nums[i-1]*res[i-1]
        
        # calculate suffix
        for i in range(n-2, -1, -1):
            suffix = nums[i+1]*suffix
            res[i] = res[i]*suffix

        # for i in range(n):
            # res[i] = prefix[i]*suffix[i]
        return res

print(Solution().productExceptSelf([1,2,3,4]))
class Solution(object):
    # Brute Force Approach with O(n2) TC and O(1) SC
    def minSubArrayLenBrute(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        currLen=0
        minLen = float('inf')
        for i in range(len(nums)):
            psum=0
            for j in range(i, len(nums)):
                psum+=nums[j]
                if psum >= target:
                    currLen = j-i+1
                    minLen = min(currLen, minLen)
        return minLen
    # Better Oproach with TC O(n) and SC O(n)
    def minSubArrayLenBetter(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        prefixSum=0
        beg=0
        minLen=float('inf')
        for idx,n in enumerate(nums):
            prefixSum+=n
            while prefixSum>=target:
                minLen = min(idx-beg+1,minLen)
                # sliding window logic
                prefixSum-=nums[beg]
                beg+=1
            
        return minLen
print(Solution().minSubArrayLenBrute(7, [2,3,1,2,4,3]))
print(Solution().minSubArrayLenBetter(4, [1,4,4]))
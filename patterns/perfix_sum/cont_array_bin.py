# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number
#  of 0 and 1.
from collections import defaultdict
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum_dict = defaultdict(int)
        prefix_sum_dict[0]=-1

        longest_subarry, prefix_sum = 0, 0
        for i,n in enumerate(nums):
            prefix_sum+=1 if n == 1 else -1

            if prefix_sum in prefix_sum_dict:
                longest_subarry = max(longest_subarry, i-prefix_sum_dict[prefix_sum])
            else:
                prefix_sum_dict[prefix_sum] = i
        
        return longest_subarry
    
nums = [1,0,0,0,0,1]

print(Solution().findMaxLength(nums))
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=0
        r=len(numbers)-1
        while l<r:
            sum = numbers[l]+numbers[r]
            if sum==target:
                return [l+1, r+1]
            elif sum > target:
                r-=1
            else:
                l+=1

numbers = [2,7,11,15]
target = 9
print(Solution().twoSum(numbers, target))
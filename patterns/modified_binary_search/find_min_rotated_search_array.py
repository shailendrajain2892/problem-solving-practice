class Solution:
    def findMin(self, nums: list[int]):
        start = 0 
        end = len(nums)-1

        min_val = float('inf')
        while start <= end:
            mid = (start+end)//2

            min_val = min(min_val, nums[mid])

            if nums[mid] < nums[end]:
                end = mid - 1
            else:
                start = mid + 1
            
        return min_val
nums = [1,2,3,4,5]
nums2 = [3,4,5,1,2]
nums3 = [5,1,2,3,4]
nums4 = [4,5,1,2,3]
n = [nums, nums2, nums3, nums4]
for i in n:
    print(f"Find min for array : {i}")
    print(Solution().findMin(i))
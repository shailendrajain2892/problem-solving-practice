from typing import List


# class Solution:
#     def merge(self, nums1, nums2):
#         l, r = 0, 0
#         merged_nums = []
#         while l < len(nums1) and r < len(nums2):
#             if nums1[l] < nums2[r]:
#                 merged_nums.append(nums1[l])
#                 l+=1
#             else:
#                 merged_nums.append(nums2[r])
#                 r+=1
#         while l < len(nums1):
#             merged_nums.append(nums1[l])
#             l+=1
#         while r < len(nums2):
#             merged_nums.append(nums2[r])
#             r+=1
#         return merged_nums
    
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         merged_nums = self.merge(nums1, nums2)
#         n = len(merged_nums)
#         if n%2 == 0:
#             return (merged_nums[n//2]+merged_nums[(n//2)-1])/2
#         else:
#             return merged_nums[n//2]
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: # type: ignore
        A, B = nums1, nums2
        total = len(A)+len(B)
        half = total//2
        
        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A)-1
        while True:
            i = (l+r)//2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i+1] if (i+1) < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j+1] if (j+1) < len(B) else float('infinity')

            if Aleft <= Bright and Bleft <= Aright:
                if total%2:
                    return min(Aright, Bright)
                return ( max(Aleft, Bleft) + min(Aright, Bright) ) / 2
            elif Aleft > Bright:
                l = i-1
            else:
                l = i+1
    


print(Solution().findMedianSortedArrays([1,2, 3, 4, 5, 6, 7], [3]))
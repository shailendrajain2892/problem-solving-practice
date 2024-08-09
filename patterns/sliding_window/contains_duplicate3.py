class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        # numList = []
        # l = 0
        # for r in range(len(nums)):
        #     i=l
        #     if abs(r-l)>indexDiff:
        #         numList.pop(0)
        #         l+=1
        #         i=l
        #     while i < r:
        #         if abs(nums[i]-nums[r])<=valueDiff:
        #             return True
        #         i+=1
        #     numList.append(nums[r])
        # return False
        # newNumswithIndex = []
        # for i, n in enumerate(nums):
        #     newNumswithIndex.append((n,i))
        
        # for j in range(len(nums)):
        #     for k in range(j+1, len(nums)):
        #         if newNumswithIndex[j][0] + valueDiff <= newNumswithIndex[k][0]:
        #             if abs(newNumswithIndex[j][1] - newNumswithIndex[k][1]) <= indexDiff:
        #                 return True
        #             else:
        #                 break
        # return False
        if valueDiff < 0: return False # edge case 
        
        seen = {}
        for i, x in enumerate(nums): 
            bkt = x//(valueDiff+1)
            if bkt in seen and i - seen[bkt][0] <= indexDiff: 
                return True 
            if bkt-1 in seen and i - seen[bkt-1][0] <= indexDiff and abs(x - seen[bkt-1][1]) <= valueDiff:
                return True 
            if bkt+1 in seen and i - seen[bkt+1][0] <= indexDiff and abs(x - seen[bkt+1][1]) <= valueDiff:
                return True 
            seen[bkt] = (i, x) 
        return False 
print(Solution().containsNearbyAlmostDuplicate(nums=[1,5,9,1,13,5],indexDiff=2,valueDiff=0))
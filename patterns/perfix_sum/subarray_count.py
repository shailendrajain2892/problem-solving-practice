from collections import defaultdict

# Brute Force Approache with TC of O(n3)
def subarraySumCountBrute(nums, k):
    psum=0
    rcount=0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            psum=0
            for l in range(i,j+1):
                psum+=nums[l]
            if psum == k:
                rcount+=1
    return rcount

# Better  Approache with TC of O(n2)
def subarraySumCountBetter(nums, k):
    psum=0
    rcount=0
    for i in range(len(nums)):
        psum=0
        for j in range(i, len(nums)):
            psum+=nums[j]
            if psum == k:
                rcount+=1
    return rcount

# Optimal Approach TC of O(n)
def subarraySumCountOptimal(nums,k):
    prefixSumCount = defaultdict(int)
    prefixSumCount[0]=1
    rcount=0
    prefixSum=0
    for n in nums:
        prefixSum+=n
        diff = prefixSum-k
        if diff in prefixSumCount:
            rcount+=prefixSumCount[diff]
            if prefixSum in prefixSumCount:
                prefixSumCount[prefixSum]+=1
            else:
                prefixSumCount[prefixSum]=1
        else:
            if prefixSum in prefixSumCount:
                prefixSumCount[prefixSum]+=1
            else:
                prefixSumCount[prefixSum]=1
    return rcount

nums=[0,1,1,1,0,1,1,1]
k = 2
print(subarraySumCountBrute(nums,k))
print(subarraySumCountBetter(nums,k))
print(subarraySumCountOptimal(nums,k))
def maxProdSubArray(nums: list[int]) -> int:
    max_so_far=float('-inf')
    max_ending_here=1
    for num in nums:
        max_ending_here = max(num*max_ending_here, num)
        max_so_far = max(max_so_far, max_ending_here)
        if max_ending_here == 0:
            max_ending_here = 1
    return max_so_far

# print(maxSubArray(nums=[-13,3,4]))

def maxProdSubArray2(nums):
    res=float('-inf')
    prod=1
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            prod=1
            for k in range(i, j+1):
                prod = prod*nums[k]
            res = max(res, prod)
    print(res)
    return res

numbers = [3,-1,4,-2]
print(maxProdSubArray(numbers))
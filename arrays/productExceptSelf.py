from functools import reduce
import operator

def productExceptSelf(nums: list[int]) -> list[int]:
    sol=[]
    for idx,num in enumerate(nums):
        sol.append(reduce(operator.mul, nums[:idx]+nums[idx+1:]))
    return sol
# print(productExceptSelf(nums=[1,2,3,4]))


def productExceptSelf2(nums: list[int]) -> list[int]:
    
    n=len(nums)
    
    left=[0]*n
    
    right=[0]*n
    
    prod=[0]*n
    
    left[0] = 1
    
    right[n-1] = 1
    
    for i in range(1, n):
        left[i] = nums[i-1] * left[i-1]
    
    # print(left)
    for j in range(n-2, -1, -1):
        right[j] = nums[j+1]*right[j+1]
    
    # print(right)
    for i in range(n):
        prod[i] = left[i] * right[i]
    
    return prod

print(productExceptSelf2(nums=[1,2,3,4]))


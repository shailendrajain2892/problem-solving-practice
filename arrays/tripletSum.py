# Brute Force Approach
def tripletSumB(nums,target):
    l = len(nums)
    ans=set()
    for i,n1 in enumerate(nums):
        for j,n2 in enumerate(nums[i+1:]):
            for k,n3 in enumerate(nums[j+1:]):
                if n1+n2+n3 == target:
                    res = (n1,n2,n3)
                    res = tuple(sorted(res))
                    ans.add(res)
    return ans

# Brute Force Approach Optimal
def tripletSumBO(nums,target):
    l = len(nums)
    ans=set()
    for i,n1 in enumerate(nums):
        for j,n2 in enumerate(nums[i+1:]):
            n3 = target-n1-n2
            if n3 in nums[j+1:]:
                # if n1+n2+n3 == target:
                res = (n1,n2,n3)
                res = tuple(sorted(res))
                ans.add(res)
    return ans

# Optimal Approach
def tripletSumO(nums, target):
    l = len(nums)
    ans = []
    for i in range(l):
        # remove duplicates
        if i!=0 and nums[i] == nums[i-1]:
            continue

        j=i+1
        k=l-1
        while j < k:
            ts = nums[i] + nums[j] + nums[k]
            if ts < target:
                j+=1
            elif ts > target:
                k-=1
            else:
                ans.append((nums[i], nums[j], nums[k]))
                j+=1
                k-=1
                while j<k and nums[j] == nums[j-1]:
                    j+=1
                while j<k and nums[k] == nums[k+1]:
                    k-=1
    return ans

numbers = [-1,0,1,2,-1,-4]
target=0
print(tripletSumBO(numbers, target))
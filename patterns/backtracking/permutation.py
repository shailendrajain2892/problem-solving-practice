# def permute(nums):
#     if len(nums) == 0:
#         return [[]]
    
#     perms = permute(nums[1:])

#     res = []
#     for p in perms:
#         for i in range(len(p)+1):
#             p_copy = p.copy()
#             p_copy.insert(i, nums[0])
#             res.append(p_copy)
#     return res

def permute(nums):
    result = []  # This will hold all the permutations
    # Base case: when there's only one number left, return it as a permutation
    if len(nums) == 1:
        return [nums[:]]  # Return a copy of nums as the only permutation

    # Iterate through each number in the list
    for i in range(len(nums)):
        # Take out the number at index i
        n = nums.pop(i)  # n is the number at index i
        # Recursively call permute on the remaining numbers
        perms = permute(nums)  # perms contains all permutations of the remaining numbers
        
        # Add the current number n to the beginning of each permutation from perms
        for perm in perms:
            result.append([n] + perm)  # Prepend n to each perm and add to result
        
        # Put the number back in its original place (important to restore the list)
        nums.insert(i, n)

    return result  # Return the final list of permutations
print(permute([1,2,3]))
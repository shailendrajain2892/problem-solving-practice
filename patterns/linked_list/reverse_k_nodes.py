def reverse(num):
    return num[::-1]

def reverse_k_node(nums, k):
    res=[]
    start = 0
    for i in range(k, len(nums)+1, k):
        res.extend(reverse(nums[start:i]))
        start+=i
    if len(res) != len(nums):
        res.extend(nums[i:len(nums)]) 
    return res

    

nums = [1,2,3,4,5,6,7,8]
print(reverse_k_node(nums, 3))
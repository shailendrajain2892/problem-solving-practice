import sys


def find_sub_array_zero_sum(num):
    prefixSum = set()
    curr_sum=0
    for i in num:
        curr_sum += i
        if curr_sum in prefixSum:
            return True
        else:
            prefixSum.add(curr_sum)
    return False

def find_sub_array_k_sum(num,k):
    prefixSum=set()
    curr_sum=0
    for i in num:
        curr_sum += i
        if curr_sum == k:
            return True
        k_sum = curr_sum-k
        if k_sum in prefixSum:
            return True
        else:
            prefixSum.add(curr_sum)
    return False

numbers = [4,2,-3,1,6]
numbers1=[4,2,0,1,6]
numbers2 = [-3,2,3,1,6]
print(find_sub_array_zero_sum(numbers2))
print(find_sub_array_k_sum(numbers2,int(sys.argv[1])))

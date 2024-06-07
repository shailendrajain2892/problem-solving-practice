def max_sub_array(num):
    max_so_far=num[0]
    curr_max = num[0]
    for i in num[1:]:
        curr_max = max(i, curr_max+i)
        max_so_far = max(curr_max, max_so_far)
    return max_so_far

n1 = [-2,1,-3,4,-1,2,1,-5,4]
n2 = [-5,-4,-1,-7,-8]
print(max_sub_array(n1))

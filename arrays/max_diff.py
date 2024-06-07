# two pointer approach
def max_diff(numbers):
    max_diff_so_far = 0 
    max_diff = 0
    i = 0
    j = i+1
    while j <= len(numbers)-1:
        if numbers[j] < numbers[i] and j < len(numbers)-1:
            i = j
            j = i+1
        else:
            max_diff_so_far = max(max_diff_so_far, numbers[j]-numbers[i])
            j += 1
        max_diff = max(max_diff, max_diff_so_far)
    return max_diff

print(max_diff([2,1,10,6,4,8]))

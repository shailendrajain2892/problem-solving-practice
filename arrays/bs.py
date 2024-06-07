def binary_search(numbers,k):
    l=0
    r=len(numbers)
    while l <= r:
        mid = (l+r)//2
        if numbers[mid] == k:
            return mid
        elif k < numbers[mid]:
            r = mid-1
        else:
            l = mid+1
    return -1

def binary_search_with_duplicates_first_Occurance(numbers,k):
    l=0
    r=len(numbers)
    while l<=r:
        m = l + (r-l)//2
        if numbers[m] == k:
            if m == 0:
                return m
            if numbers[m-1]!=k:
                return m
            else:
                r = m-1
        elif k < m:
            r = m-1
        else:
            l = m+1
    return -1


def binary_search_with_duplicates_last_occurance(numbers,k):
    l=0
    r=len(numbers)
    while l<=r:
        m = l + (r-l)//2
        if numbers[m] == k:
            if m == len(numbers)-1:
                return m
            if numbers[m+1]!=k:
                return m
            else:
                l = m+1
        elif k < m:
            r = m-1
        else:
            l = m+1
    return -1

print(binary_search([2,5,6,8,12,14],5))
print(binary_search_with_duplicates_first_Occurance([0,1,1,2,2,2],2))
print(binary_search_with_duplicates_last_occurance([0,1,1,2,2,2],2))

def get_previous_smaller_elements(num):
    res=[]
    stack=[]
    for idx, n in enumerate(num):
        while(len(stack)!=0 and num[stack[-1]]>=n):
            stack.pop()
        res.append(-1) if len(stack)==0 else res.append(stack[-1])
        stack.append(idx)
    return res

def get_next_smaller_elements(num):
    res=[]
    stack=[]
    for idx in range(len(num)-1,-1,-1):
        while(len(stack) != 0 and num[stack[-1]]>=num[idx]):
            stack.pop()
        res.append(len(num)) if len(stack)==0 else res.append(stack[-1])
        stack.append(idx)
    return [i for i in reversed(res)]

def max_area_histrogram(heights):
    previous_smaller_elements = get_previous_smaller_elements(heights)
    next_smaller_elements = get_next_smaller_elements(heights)
    print(f"heights: {heights}")
    print(f"previous smaller elements : {previous_smaller_elements}")
    print(f"next smaller elements : {next_smaller_elements}")
    max_area = 0
    for idx,h in enumerate(heights):
        curr_area = (next_smaller_elements[idx]-previous_smaller_elements[idx]-1)*h
        max_area = max(curr_area, max_area)
    return max_area
heights=[2,1,5,6,2,3]
heights1=[2,4,6]
print(max_area_histrogram(heights1))
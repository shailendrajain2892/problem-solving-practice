def prev_greater_element(numbers):
    res=[]
    stack=[]
    for n in numbers:
        while(len(stack) != 0 and stack[-1] <= n ):
            stack.pop()
        res.append(-1) if len(stack)==0 else res.append(stack[-1])
        stack.append(n)
    return res



def prev_smaller_element(numbers):
    res=[]
    stack=[]
    for n in numbers:
        while(len(stack) != 0 and stack[-1] >= n ):
            stack.pop()
        res.append(-1) if len(stack)==0 else res.append(stack[-1])
        stack.append(n)
    return res


num = [10,4,2,20,40,12,30]
print(prev_greater_element(num))
print(prev_smaller_element(num))
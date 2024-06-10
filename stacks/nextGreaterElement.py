def next_greater_element(numbers):
    res=[]
    stack=[]
    for n in reversed(numbers):
        while(len(stack) != 0 and stack[-1] <= n ):
            stack.pop()
        res.append(-1) if len(stack)==0 else res.append(stack[-1])
        stack.append(n)
    return reversed(res)

def next_smaller_element(numbers):
    res=[]
    stack=[]
    for n in reversed(numbers):
        while(len(stack) != 0 and stack[-1] >= n ):
            stack.pop()
        res.append(-1) if len(stack)==0 else res.append(stack[-1])
        stack.append(n)
    return reversed(res)

num = [4,5,2,25]
print(f"next greater element : {[n for n in next_greater_element(num)]}")
print(f"next smaller element : {[n for n in next_smaller_element(num)]}")

def stock_span(stock):
    res=[]
    stack=[]
    for idx,s in enumerate(stock):
        while (len(stack) != 0 and stock[stack[-1]]<=s):
            stack.pop()

        res.append(idx+1) if len(stack)==0 else res.append(idx-stack[-1])
        stack.append(idx)

    return res
stock = [100,80,60,70,60,75,85]
print(stock_span(stock))
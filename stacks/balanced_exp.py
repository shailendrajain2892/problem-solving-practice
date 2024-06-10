def matching(a, b):
    if (a=='(' and b == ')' ) or (a=='[' and b == ']') or (a=='{' and b=="}"):
        return True
    else:
        return False
def check_balance_pattern(exp):
    stack=[]
    for e in exp:
        if e in ['(','[','{']:
            stack.append(e)
        else:
            if len(stack) == 0:
                return False
            elif not matching(stack[-1:][0], e):
                return False
            else:
                stack.pop()

    if len(stack) != 0:
        return False
    return True

print(check_balance_pattern('{()}[]'))
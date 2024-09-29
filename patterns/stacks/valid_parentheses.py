from collections import deque
class Solution:
    def compareParenth(self, stack, rightBrkt):
        if not stack:
            return False
        leftBrkt = stack.pop()
        if leftBrkt == '(' and rightBrkt == ')':
            return True
        elif leftBrkt == '{' and rightBrkt == '}':
            return True
        elif leftBrkt == '[' and rightBrkt == ']':
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        openBrackets = ['(', '[', '{']
        stack = []
        for c in s:
            if c in openBrackets:
                stack.append(c)
            elif self.compareParenth(stack, c) == False:
                return False
        if not stack:
            return True
        else:
            return False
    
for s in ["(){}}{", '((',']]','[]', '([{}])', '[(])', '()[]{}', '()[{}]']:
    print(Solution().isValid(s))
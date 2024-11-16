from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"])
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue
            y, x = stack.pop(), stack.pop()
            if token == "+":
                res = x+y
            elif token == "*":
                res = x*y
            elif token == "-":
                res = x-y
            elif token == "/" :
                res = int(x/y)
            stack.append(res)
        return stack[0]

tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))
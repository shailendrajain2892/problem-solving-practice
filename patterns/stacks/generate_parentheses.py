from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(openC, closeC):
            if openC == closeC == n:
                res.append("".join(stack))
                return
            
            if closeC < openC:
                stack.append(")")
                backtrack(openC, closeC+1)
                stack.pop()

            if openC <= n-1:
                stack.append("(")
                backtrack(openC+1, closeC)
                stack.pop()



        backtrack(0, 0)
        print(len(res))
        return res
    
print(Solution().generateParenthesis(3))
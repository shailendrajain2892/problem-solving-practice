from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        positiveDiag = set()
        negativeDiag = set()
        board = [['.']*n for _ in range(n)]
        res = []
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
            
            for c in range(n):
                if c in col or (r+c) in positiveDiag or (r-c) in negativeDiag:
                    continue
                
                board[r][c] = "Q"
                col.add(c)
                positiveDiag.add(r+c)
                negativeDiag.add(r-c)

                backtrack(r+1)

                col.remove(c)
                positiveDiag.remove(r+c)
                negativeDiag.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res                

print(Solution().solveNQueens(4))

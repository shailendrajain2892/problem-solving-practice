class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        path = set()
        def backtrack(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                r >= len(board) or c >= len(board[0]) or
                board[r][c] != word or
                (r,c) in path):
                return False
            
            path.add((r,c))
            if (backtrack(r, c+1, i+1) or 
                   backtrack(r, c-1, i+1) or 
                   backtrack(r+1, c, i+1) or 
                   backtrack(r-1, c+1, i+1) ):
                return True

            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        if backtrack(i, j, 0):
                            return True
            return False
            
            
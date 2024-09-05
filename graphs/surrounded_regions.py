from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        if m == 1 and n == 1:
            return
        if m == 0 or n == 0:
            return

        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != "O":
                return

            board[row][col] = "T"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Identify all O's which are on edge as those can't be surrouned and connected to it
        for i in range(n):
            # top boundary
            if board[0][i] == "O":
                dfs(0, i)
            # right boundary
            if board[i][n - 1] == "O":
                dfs(i, n - 1)
        for i in range(m):
            # left boundary
            if board[i][0] == "O":
                dfs(i, 0)
            # bottom boundary
            if board[m - 1][i] == "O":
                dfs(m - 1, i)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
board1 = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
Solution().solve(board)
print(board)
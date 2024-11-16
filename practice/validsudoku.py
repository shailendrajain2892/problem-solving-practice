from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet, colSet, subboxSet = defaultdict(list), defaultdict(list), defaultdict(list)
        m, n = len(board), len(board[0])
        for row in range(m):
            for col in range(n):
                val = board[row][col]
                if val == ".":
                    continue
                if val in rowSet[row] or val in colSet[col] or val in subboxSet[(row//3, col//3)]:
                    return False
                rowSet[row].append(val)
                colSet[col].append(val)
                subboxSet[(row//3, col//3)].append(val)
        return True

board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(board))
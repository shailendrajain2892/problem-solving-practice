from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap, colMap, subboxMap = defaultdict(list), defaultdict(list),  defaultdict(list)
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == ".":
                    continue
                num = int(board[row][col])
                subbox = (row//3,col//3)
                if (num in rowMap[row] or
                  num in colMap[col] or
                   num in subboxMap[subbox]):
                    return False
                rowMap[row].append(num)
                colMap[col].append(num)
                subboxMap[subbox].append(num)
        return True

sudoku = [["1","2",".",".","3",".",".",".","."],
          ["4",".",".","5",".",".",".",".","."],
          [".","9","8",".",".",".",".",".","3"],
          ["5",".",".",".","6",".",".",".","4"],
          [".",".",".","8",".","3",".",".","5"],
          ["7",".",".",".","2",".",".",".","6"],
          [".",".",".",".",".",".","2",".","."],
          [".",".",".","4","1","9",".",".","8"],
          [".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(sudoku))
            
# class Solution:
#     def DFS(self, ans, row, col, existingColor, newColor, delRow, delCol):
#         ans[row][col] = newColor
#         for i in range(4):
#             nrow = row + delRow[i]
#             ncol = col + delCol[i]
#             if nrow >=0 and nrow < len(ans) and ncol >= 0 and ncol < len(ans[0]):
#                 if ans[nrow][ncol] == existingColor and ans[nrow][ncol] != newColor:
#                     self.DFS(ans, nrow, ncol, existingColor, newColor, delRow, delCol)
        
#     def floodFill(
#         self, image: list[list[int]], sr: int, sc: int, color: int
#     ) -> list[list[int]]:
#         iniColor = image[sr][sc]
#         delRow = [-1, 0, 1, 0]
#         delCol = [0, -1, 0, 1]
#         ans = image
#         self.DFS(ans, sr, sc, iniColor, color, delRow, delCol)
#         return ans
    
from typing import List


class Solution:

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        initColor = image[sr][sc]

        if image[sr][sc] == color:
            return image

        def dfs(r, c):
            if (
                r < 0
                or r >= len(image)
                or c < 0
                or c >= len(image[0])
                or image[r][c] != initColor
            ):
                return

            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)

        return image


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
print(Solution().floodFill(image, sr, sc, color))

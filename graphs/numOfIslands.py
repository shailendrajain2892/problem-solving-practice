from typing import List


class Solution:
    def DFS(self, grid, i, j, visited, totalRows, totalCols):

        directions = [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]

        for i, j in directions:
            if (i,j) not in visited and i >= 0 and i < totalRows and j >= 0 and j < totalCols and grid[i][j] == '1':
                visited.add((i, j))
                self.DFS(grid, i, j, visited, totalRows, totalCols)

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        numOfIsland = 0
        totalRows = len(grid)
        totalCols = len(grid[0])
        for i in range(totalRows):
            for j in range(totalCols):
                if (i, j) not in visited and grid[i][j] == '1':
                    visited.add((i,j))
                    self.DFS(grid, i, j, visited, totalRows, totalCols)
                    numOfIsland += 1
        return numOfIsland

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid1 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
islands = Solution().numIslands(grid1)
print(islands)
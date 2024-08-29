import queue
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        fresh, q = 0, queue.Queue()
        time = 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1:
                    fresh+=1
                if grid[m][n] == 2:
                    q.put((m,n))
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while not q.empty() and fresh > 0:
            for i in range(q.qsize()):
                r, c = q.get()
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if row < 0 or col < 0 or row == len(grid) or col == len(grid) or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    q.put((row,col))
                    fresh-=1
            time+=1
        
        return time if fresh == 0 else -1
    

print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
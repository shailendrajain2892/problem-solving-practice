class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix: 
            return False
        
        row, col = 0, len(matrix[0])-1
        
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col-=1
            else:
                row+=1
            
        return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 10
print(Solution().searchMatrix(matrix, target))
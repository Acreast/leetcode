# Last updated: 8/29/2025, 12:34:31 AM
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for d in range(n - 2 , -1, -1):
            diag = sorted(grid[i][i + d] for i in range(n - d))
            for i, num in enumerate(diag):
                grid[i][i + d] = num
        
        for d in range(n - 1):
            diag = sorted((grid[j + d][j] for j in range(n - d)), reverse=True)
            for i, num in enumerate(diag):
                grid[i + d][i] = num

        
        return grid
# Last updated: 7/12/2025, 11:52:10 PM
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)    
        COLS = len(matrix[0])
        res = 0
        cache = {}
        def dfs(r,c):
            if c == COLS or r == ROWS or not matrix[r][c]:
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            cache[(r,c)] = 1 + min(
                dfs(r + 1, c),
                dfs(r, c + 1),
                dfs(r + 1, c + 1)
            )

            return cache[(r,c)]

        for i in range(ROWS):
            for j in range(COLS):
                res += dfs(i,j)
        return res
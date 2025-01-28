class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r, c) in visit):
                return 0
            visit.add((r,c))
            res = grid[r][c]
            nei = [
                [r + 1, c],
                [r - 1, c],
                [r, c + 1],
                [r, c - 1],
            ]
            for nr,nc in nei:
                res += dfs(nr,nc)
            return res
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(dfs(r, c), res)
        
        return res
        
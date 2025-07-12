# Last updated: 7/12/2025, 11:52:13 PM
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rows = [0] * ROWS
        cols = [0] * COLS 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and max(rows[r], cols[c]) > 1:
                    res += 1

        return res

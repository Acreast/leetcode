# Last updated: 7/12/2025, 11:54:41 PM
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        for r in range(ROW):
            if grid[r][0] == 0:
                for c in range(COL):
                    grid[r][c] = 0 if grid[r][c] else 1

        for c in range(COL):
            one_count = 0
            for r in range(ROW):
                one_count += grid[r][c]
            if one_count < ROW - one_count:
                for r in range(ROW):
                    grid[r][c] = 0 if grid[r][c] else 1

        res = 0
        for r in range(ROW):
            for c in range(COL):
                res += grid[r][c] << (COL - c - 1)

        return res
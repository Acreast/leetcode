# Last updated: 12/28/2025, 3:08:40 PM
1class Solution:
2    def countNegatives(self, grid: List[List[int]]) -> int:
3        negatives = 0
4        ROWS = len(grid)
5        COLS = len(grid[0])
6        for r in range(ROWS):
7            next_row_flag = False
8            for c in range(COLS):
9                if grid[r][c] < 0:
10                    negatives += COLS - c
11                    next_row_flag = True
12                    break
13            if next_row_flag == True:
14                continue
15
16        return negatives
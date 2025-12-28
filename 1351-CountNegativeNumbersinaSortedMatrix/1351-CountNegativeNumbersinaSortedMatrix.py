# Last updated: 12/28/2025, 4:00:33 PM
1class Solution:
2    def countNegatives(self, grid: List[List[int]]) -> int:
3        negatives = 0
4        ROWS = len(grid)
5        COLS = len(grid[0])
6
7        row = ROWS - 1
8        col = 0
9
10        while row >= 0 and col < COLS:
11            if grid[row][col] < 0:
12                negatives += COLS - col
13                row -= 1
14            else:
15                col += 1
16
17        return negatives
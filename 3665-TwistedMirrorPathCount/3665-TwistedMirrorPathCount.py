# Last updated: 11/1/2026, 12:38:25 AM
1class Solution:
2    def uniquePaths(self, grid: List[List[int]]) -> int:
3        mod = 10**9 + 7
4        down = [1] + [0] * (len(grid[0]) - 1)  # d: paths coming into each cell from above
5        for row in grid:
6            right = 0  # r: paths coming in from the left
7            for j, mirror in enumerate(row):
8                if mirror:  # a mirror swaps the flows
9                    right, down[j] = down[j], right
10                else:  # an empty cell merges them
11                    right = down[j] = (right + down[j]) % mod
12        return down[-1]
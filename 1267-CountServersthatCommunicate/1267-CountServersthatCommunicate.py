# Last updated: 11/9/2026, 1:34:09 AM
1class Solution:
2    def countServers(self, grid: list[list[int]]) -> int:
3        rows = [sum(row) for row in grid]  # servers on each row
4        cols = [sum(col) for col in zip(*grid)]  # servers on each column
5
6        ans = 0
7        for i, row in enumerate(grid):
8            for j, server in enumerate(row):
9                if server and rows[i] + cols[j] > 2:  # it's counted in both, so more than 2 means company
10                    ans += 1
11        return ans
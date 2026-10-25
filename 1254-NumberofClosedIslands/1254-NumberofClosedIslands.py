# Last updated: 10/26/2026, 1:34:11 AM
1class Solution:
2    def closedIsland(self, grid: List[List[int]]) -> int:
3        m, n = len(grid), len(grid[0])
4
5        def closed(i, j):  # flood the island through (i, j); True if it never reaches the border
6            if not (0 <= i < m and 0 <= j < n):
7                return False  # stepped off the grid: the island touches the border
8            if grid[i][j]:
9                return True  # water, or land we already flooded
10            grid[i][j] = 1  # visited: turn it into water
11            return closed(i + 1, j) & closed(i - 1, j) & closed(i, j + 1) & closed(i, j - 1)  # & (not and) floods all 4 sides
12
13        return sum(closed(i, j) for i, j in product(range(m), range(n)) if not grid[i][j])
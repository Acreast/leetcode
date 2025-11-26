# Last updated: 11/26/2025, 9:55:57 PM
1class Solution:
2    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
3        ROWS = len(grid)
4        COLS = len(grid[0])
5        cache = [[[-1] * k for _ in range(COLS)] for _ in range(ROWS)]
6        MOD = 10 ** 9 + 7
7        def dfs(r, c, remain):
8            if r == ROWS - 1 and c == COLS - 1:
9                remain = (remain + grid[r][c]) % k
10                return 0 if remain else 1
11            if r == ROWS or c == COLS:
12                return 0
13            if cache[r][c][remain] > -1:
14                return cache[r][c][remain]
15            cache[r][c][remain] = (
16                dfs(r + 1, c, (remain + grid[r][c]) % k) +
17                dfs(r, c + 1, (remain + grid[r][c]) % k)
18            )
19            return cache[r][c][remain]
20
21        return dfs(0, 0, 0) % MOD
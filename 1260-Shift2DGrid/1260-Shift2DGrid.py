# Last updated: 7/21/2026, 1:08:30 AM
1class Solution:
2    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
3        if not k: return grid
4        r, c = len(grid), len(grid[0])
5        n = r * c
6        k %= n
7        if not k: return grid
8
9        def shift(i, j):
10            while i < j:
11                grid[i // c][i % c], grid[j // c][j % c] = grid[j // c][j % c], grid[i // c][i % c]
12                i += 1
13                j -= 1
14            
15        shift(0, n - 1)
16        shift(0, k - 1)
17        shift(k, n - 1)
18
19        return grid
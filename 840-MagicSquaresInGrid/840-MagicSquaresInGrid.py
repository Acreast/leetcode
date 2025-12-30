# Last updated: 12/30/2025, 9:13:33 PM
1class Solution:
2    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
3        
4        def is_magic(i, j):
5            unique = set()
6            row_sum = [0] * 3
7            col_sum = [0] * 3
8
9            for r in range(i - 1, i + 2):
10                for c in range(j - 1, j + 2):
11                    v = grid[r][c]
12
13                    if v < 1 or v > 9 or v in unique:
14                        return False
15
16                    unique.add(v)
17                    row_sum[r - (i - 1)] += v
18                    col_sum[c - (j - 1)] += v
19
20            if unique != set(range(1, 10)):
21                return False
22
23            if any(s != 15 for s in row_sum):
24                return False
25            if any(s != 15 for s in col_sum):
26                return False
27
28            return (
29                grid[i-1][j-1] + grid[i+1][j+1] == 10 and
30                grid[i+1][j-1] + grid[i-1][j+1] == 10
31            )
32
33        r, c = len(grid), len(grid[0])
34        if r < 3 or c < 3:
35            return 0
36
37        count = 0
38        for i in range(1, r - 1):
39            for j in range(1, c - 1):
40                if grid[i][j] == 5 and is_magic(i, j):
41                    count += 1
42        return count
43
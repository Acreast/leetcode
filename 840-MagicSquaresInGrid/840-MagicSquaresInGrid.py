# Last updated: 12/30/2025, 10:48:01 PM
1class Solution:
2    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
3        
4        def is_magic(i, j):
5            unique_integers = set()
6            row_sum = [0] * 3
7            col_sum = [0] * 3
8
9            for row in range(i - 1, i + 2):
10                for col in range(j - 1, j + 2):
11                    value = grid[row][col]
12                    if value < 1 or value > 9:
13                        return False
14                    
15                    if value in unique_integers:
16                        return False
17                    else:
18                        unique_integers.add(value)
19                        
20                    row_sum[row-i + 1] += value
21                    col_sum[col-j + 1] += value
22
23            if unique_integers != set(range(1, 10)):
24                return False
25            
26            for sum in row_sum:
27                if sum != 15: return False
28            for sum in col_sum:
29                if sum != 15: return False
30                    
31            return (
32                grid[i-1][j-1] + grid[i+1][j+1] == 10 and
33                grid[i+1][j-1] + grid[i-1][j+1] == 10
34            )
35
36        r, c = len(grid), len(grid[0])
37
38        if r < 3 or c < 3:
39            return 0
40        
41        count = 0
42        for i in range(1, r - 1):
43            for j in range(1, c - 1):
44                if grid[i][j] == 5 and is_magic(i, j):
45                    count += 1
46        return count
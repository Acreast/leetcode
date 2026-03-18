// Last updated: 3/18/2026, 11:45:54 PM
1class Solution {
2    public int countSubmatrices(int[][] grid, int k) {
3        int m = grid.length, n = grid[0].length;
4        int count = 0;
5
6        for (int i = 0; i < m; i ++) {
7            for (int j = 0; j < n; j ++) {
8                if ( i > 0) {
9                    grid[i][j] += grid[i - 1][j];
10                }
11                if (j > 0){
12                    grid[i][j] += grid[i][j - 1];
13                }
14                if (i >0 && j > 0) {
15                    grid[i][j] -= grid[i -1][j - 1];
16                }
17                if (grid[i][j] <= k) {
18                    count ++;
19                }
20
21            }
22        }   
23        return count;
24    }
25}
// Last updated: 3/24/2026, 5:07:33 PM
1class Solution {
2    public int[][] constructProductMatrix(int[][] grid) {
3        int m = grid.length;
4        int n = grid[0].length;
5        int MOD = 12345;
6
7        int[][] res = new int[m][n];
8        int pref =1;
9        int suff = 1;
10
11        for (int i = 0; i < m; i ++) {
12            for (int j = 0; j < n; j ++) {
13                res[i][j] = pref;
14                pref = (int)((long)pref * grid[i][j] % MOD);
15            }
16        }
17
18        for (int i = m - 1; i >= 0; i--) {
19            for (int j = n - 1; j >= 0; j--) {
20                res[i][j] = (int)((long)res[i][j] * suff % MOD);
21                suff = (int)((long)suff * grid[i][j] % MOD);
22            }
23        }
24
25        return res;
26    }
27}
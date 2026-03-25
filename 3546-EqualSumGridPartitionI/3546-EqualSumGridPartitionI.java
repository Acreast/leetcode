// Last updated: 3/26/2026, 12:26:56 AM
1class Solution {
2    public boolean canPartitionGrid(int[][] grid) {
3        int m = grid.length;
4        int n = grid[0].length;
5
6        long[] row_sum = new long[m];
7        long[] col_sum = new long[n];
8
9
10        for (int i = 0; i < m; i ++) {
11            for (int j = 0; j < n;j ++) {
12                int val = grid[i][j];
13                row_sum[i] += val;
14                col_sum[j] += val;
15            }
16        }
17
18        long[] row_prefix = new long[m + 1];
19        for (int i = 0; i < m; i ++) {
20            row_prefix[i + 1] = row_prefix[i] + row_sum[i];
21        }
22
23        long[] col_prefix = new long[n + 1];
24        for (int i = 0; i < n; i ++) {
25            col_prefix[i + 1] = col_prefix[i] + col_sum[i];
26        }
27
28        long total_sum = row_prefix[m];
29
30        if (total_sum % 2 != 0) {
31            return false;
32        }
33
34        long target = total_sum /2;
35
36        for (int i = 1; i < m; i ++) {
37            if(row_prefix[i] == target) {
38                return true;
39            }
40        }
41
42        for (int i = 1; i < n; i ++) {
43            if (col_prefix[i] ==  target) {
44                return true;
45            }
46        }
47
48        return false;
49    }
50}
// Last updated: 3/27/2026, 12:41:19 AM
1class Solution {
2    static final int BIG_NUM = 100001;
3
4    public boolean canPartitionGrid(int[][] grid) {
5        int m = grid.length, n = grid[0].length; long total = 0;
6
7        int[] bottom = new int[BIG_NUM], top = new int[BIG_NUM]; 
8        for (int[] row : grid) {
9            for (int x : row) {
10                total += x;
11                bottom[x]++;
12            }
13        }
14
15        long top_sum = 0;
16        for (int i = 0; i < m - 1; i++) {
17            for (int j = 0; j < n; j++) {
18                int val = grid[i][j];
19                top_sum += val;
20                top[val]++;
21                bottom[val]--;
22            }
23
24
25            long bottom_sum = total - top_sum;
26            if (top_sum == bottom_sum) return true;
27
28            long diff = Math.abs(top_sum - bottom_sum);
29            if (diff < BIG_NUM) {
30                if (top_sum > bottom_sum) {
31                    if (check(top, grid, 0, i, 0, n - 1, diff)) {
32                        return true;
33                    }
34                } else {
35                    if (check(bottom, grid, i + 1, m - 1, 0, n - 1, diff)) {
36                        return true;
37                    }
38                }
39            }
40        }
41
42        int[] left = new int[BIG_NUM], right = new int[BIG_NUM];
43        for (int[] row : grid) {
44            for (int x : row) {
45                right[x]++;
46            }
47        }
48
49        long left_sum = 0;
50        for (int j = 0; j < n - 1; j++) {
51            for (int i = 0; i < m; i++) {
52                int val = grid[i][j];
53                left_sum += val;
54                left[val]++;
55                right[val]--;
56            }
57
58            long right_sum = total - left_sum;
59            if (left_sum == right_sum) {
60                return true;
61            }
62
63            long diff = Math.abs(left_sum - right_sum);
64            if (diff < BIG_NUM) {
65                if (left_sum > right_sum) {
66                    if (check(left, grid, 0, m - 1, 0, j, diff)) {
67                        return true;
68                    }
69                } else {
70                    if (check(right, grid, 0, m - 1, j + 1, n - 1, diff)) {
71                        return true;
72                    }
73                }
74            }
75        }
76
77        return false;
78    }
79
80    private boolean check(int[] sum, int[][] grid, int r1, int r2, int c1, int c2, long diff) {
81        int rows = r2 - r1 + 1, cols = c2 - c1 + 1;
82
83        if (rows * cols == 1) return false;
84
85        if (rows > 1 && cols > 1) {
86            return sum[(int)diff] > 0;
87        }
88
89        if (rows == 1) {
90            return grid[r1][c1] == diff || grid[r2][c2] == diff;
91        } else {
92            return grid[r1][c1] == diff || grid[r2][c1] == diff;
93        }
94    }
95}
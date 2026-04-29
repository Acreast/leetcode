// Last updated: 4/29/2026, 11:50:09 PM
1class Solution {
2    public long maximumScore(int[][] grid) {
3        int n = grid.length, m = grid[0].length;
4        if (m == 1) return 0;
5
6        long[][] col = new long[m][n + 1];
7
8        for (int j = 0; j < m; j ++) {
9            for (int i =0; i < n; i ++) {
10                col[j][i + 1] = col[j][i] + grid[i][j];
11            }
12        }
13
14
15        long[][] dp = new long[n + 1][n + 1];
16        long[][] prefMax = new long[n + 1][n + 1];
17        long[][] suffMax = new long[n + 1][n + 1];
18
19        for (int c = 1; c < m; c++) {
20            long[][] newdp = new long[n + 1][n + 1];
21
22            for (int curr = 0; curr <= n; curr ++) {
23                for (int prev = 0; prev <= n; prev ++) {
24                    
25                    if (curr <= prev) {
26                        long gain = col[c][prev] - col[c][curr];
27
28                        newdp[curr][prev] = Math.max(
29                            newdp[curr][prev],
30                            suffMax[prev][0] + gain
31                        );
32                    } else {
33                        long gain = col[c - 1][curr] - col[c - 1][prev];
34
35                        newdp[curr][prev] = Math.max(
36                            newdp[curr][prev],
37                            Math.max(
38                                suffMax[prev][curr],
39                                prefMax[prev][curr] + gain
40                            )
41                        );
42                    }
43
44                }
45            }
46
47            for (int curr = 0; curr <= n; curr ++) {
48                prefMax[curr][0] = newdp[curr][0];
49
50                for (int prev = 1; prev <= n; prev++) {
51                    long penalty = 0;
52                    if (prev > curr) 
53                        penalty = col[c][prev] - col[c][curr];
54
55                    prefMax[curr][prev] = Math.max(
56                        prefMax[curr][prev - 1],
57                        newdp[curr][prev] - penalty
58                    );
59                }
60                
61                suffMax[curr][n] = newdp[curr][n];
62
63                for (int prev = n - 1; prev >= 0; prev --) {
64                    suffMax[curr][prev] = Math.max(
65                        suffMax[curr][prev + 1],
66                        newdp[curr][prev]
67                    );
68                }
69            }
70
71            dp = newdp;
72
73        }
74
75        long res = 0;
76        for (int k = 0; k <= n; k ++) {
77            res = Math.max(res, Math.max(dp[0][k],dp[n][k]));
78        }
79
80        return res;
81    }
82}
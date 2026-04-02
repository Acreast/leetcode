// Last updated: 4/2/2026, 11:59:04 PM
1class Solution {
2    public int maximumAmount(int[][] coins) {
3        int m = coins.length;
4        int n = coins[0].length;
5        
6        int [][][] dp = new int[m][n][3];
7
8        for (int i = 0; i < m;i ++) {
9            for (int j = 0; j < n; j ++) {
10                Arrays.fill(dp[i][j], Integer.MIN_VALUE);
11            }
12        }
13
14        dp[0][0][0] = coins[0][0];
15
16        if (coins[0][0] < 0) {
17            dp[0][0][1] = 0;
18        }
19
20        for (int i = 0; i < m; i ++) {
21            for(int j = 0; j < n; j ++) {
22                if (i == 0 && j == 0) continue;
23                    for (int used = 0; used < 3; used++) {
24                        int best = Integer.MIN_VALUE;
25
26                        // ---- Come from the TOP cell (i-1, j) ----
27                        if (i > 0) {
28                            // Option 1: Do NOT neutralise current cell
29                            if (dp[i-1][j][used] != Integer.MIN_VALUE) {
30                                int val = dp[i-1][j][used] + coins[i][j];
31                                best = Math.max(best, val);
32                            }
33                            // Option 2: Neutralise current cell (only if we have a neutralisation left
34                            //           and the current cell is actually a robber)
35                            if (used > 0 && coins[i][j] < 0) {
36                                if (dp[i-1][j][used-1] != Integer.MIN_VALUE) {
37                                    int val = dp[i-1][j][used-1] + 0; // neutralise -> add 0
38                                    best = Math.max(best, val);
39                                }
40                            }
41                        }
42
43                        // ---- Come from the LEFT cell (i, j-1) ----
44                        if (j > 0) {
45                            // Option 1: Do NOT neutralise
46                            if (dp[i][j-1][used] != Integer.MIN_VALUE) {
47                                int val = dp[i][j-1][used] + coins[i][j];
48                                best = Math.max(best, val);
49                            }
50                            // Option 2: Neutralise (if possible)
51                            if (used > 0 && coins[i][j] < 0) {
52                                if (dp[i][j-1][used-1] != Integer.MIN_VALUE) {
53                                    int val = dp[i][j-1][used-1] + 0;
54                                    best = Math.max(best, val);
55                                }
56                            }
57                        }
58
59                        // Store the best value for this cell and this number of neutralisations
60                        dp[i][j][used] = best;
61                    }
62            }
63        }
64
65        return Math.max(dp[m - 1][n -1][0], Math.max(dp[m-1][n-1][1], dp[m-1][n-1][2]));
66    }
67}
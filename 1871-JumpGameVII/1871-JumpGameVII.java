// Last updated: 5/26/2026, 12:34:23 AM
1class Solution {
2    public boolean canReach(String s, int minJ, int maxJ) {
3        int n = s.length();
4
5        if (s.charAt(n - 1) == '1')
6            return false;
7
8        int[] dp = new int[n];
9        dp[0] = 1;
10        int reach = 0, maxR = maxJ;
11
12        for (int i = minJ; i < n; i++) {
13            if (i > maxR) return false;
14
15            reach += dp[i - minJ];
16            if (i > maxJ) reach -= dp[i - maxJ - 1];
17
18            if (reach > 0 && s.charAt(i) == '0') {
19                dp[i] = 1;
20                maxR = i + maxJ;
21            }
22        }
23
24        return reach > 0;
25    }
26}
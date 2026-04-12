// Last updated: 4/12/2026, 11:49:33 PM
1class Solution {
2    int cal( int a, int b) {
3        return Math.abs(a/ 6 -b / 6) + Math.abs(a % 6 - b % 6);
4    }
5
6    public int minimumDistance(String word) {
7        int n = word.length();
8        int [][][] dp = new int[n + 1][26][26];
9
10        for (int i = 0; i < n ; i ++) {
11            int t = word.charAt(i) - 'A';
12
13            for (int j = 0; j < 26; j ++) {
14                for (int k = 0; k < 26; k ++) {
15                    dp[i + 1][j][k] = 1000000;
16                }
17            }
18
19            for (int j = 0; j < 26; j ++) {
20                for (int k = 0; k < 26; k ++) {
21                    dp[i + 1][j][t] = Math.min(dp[i + 1][j][t], dp[i][j][k] + cal(k,t));
22                    dp[i + 1][t][k] = Math.min(dp[i + 1][t][k], dp[i][j][k] + cal(j,t));
23                }
24            }
25        }
26
27        int ans = 1000000;
28        for ( int j = 0; j < 26; j ++) {
29            for (int k = 0; k < 26; k ++) {
30                ans = Math.min(ans, dp[n][j][k]);
31            }
32        }
33        return ans;
34    }
35}
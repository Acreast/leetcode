// Last updated: 5/25/2026, 12:49:33 AM
1class Solution {
2    int[] dp;
3
4    public int maxJumps(int[] arr, int d) {
5        int n = arr.length;
6        dp = new int[n];
7
8        int ans = 1;
9
10        for (int i = 0; i < n; i++) {
11            ans = Math.max(ans, dfs(i, arr, d));
12        }
13
14        return ans;
15    }
16
17    private int dfs(int i, int[] arr, int d) {
18        if (dp[i] != 0)
19            return dp[i];
20
21        int best = 1;
22
23        for (int nxt = i + 1; nxt <= Math.min(arr.length - 1, i + d); nxt++) {
24            if (arr[nxt] >= arr[i])
25                break;
26
27            best = Math.max(best, 1 + dfs(nxt, arr, d));
28        }
29
30        for (int nxt = i - 1; nxt >= Math.max(0, i - d); nxt--) {
31            if (arr[nxt] >= arr[i])
32                break;
33
34            best = Math.max(best, 1 + dfs(nxt, arr, d));
35        }
36
37        return dp[i] = best;
38    }
39}
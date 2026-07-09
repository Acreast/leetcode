// Last updated: 7/10/2026, 1:41:32 AM
1class Solution {
2    public boolean[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
3        int[] component = new int[n];
4
5        int val = 0;
6        component[0] = 0;
7
8        for (int i = 1; i < n; i++) {
9            if (nums[i] - nums[i - 1] > maxDiff) {
10                val++;
11            }
12            component[i] = val;
13        }
14
15        boolean[] ans = new boolean[queries.length];
16
17        for (int i = 0; i < queries.length; i++) {
18            int u = queries[i][0];
19            int v = queries[i][1];
20            ans[i] = component[u] == component[v];
21        }
22
23        return ans;
24    }
25}
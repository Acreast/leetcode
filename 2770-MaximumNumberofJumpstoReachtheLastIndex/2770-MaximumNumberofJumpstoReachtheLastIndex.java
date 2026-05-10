// Last updated: 5/11/2026, 1:19:02 AM
1class Solution {
2    public int maximumJumps(int[] nums, int target) {
3
4        int n = nums.length;
5
6        // dp[i] stores maximum jumps to reach index i
7        int[] dp = new int[n];
8
9        // Mark all indices unreachable
10        Arrays.fill(dp, -1);
11
12        // Starting index needs 0 jumps
13        dp[0] = 0;
14
15        for(int i = 1; i < n; i++) {
16
17            // Check all previous indices
18            for(int j = 0; j < i; j++) {
19
20                // Valid jump and previous index reachable
21                if(Math.abs(nums[i] - nums[j]) <= target && dp[j] != -1) {
22
23                    // Update maximum jumps
24                    dp[i] = Math.max(dp[i], dp[j] + 1);
25                }
26            }
27        }
28
29        return dp[n - 1];
30    }
31}
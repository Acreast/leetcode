// Last updated: 9/22/2026, 1:54:16 AM
1#include <vector>
2
3using namespace std;
4
5class Solution {
6public:
7    vector<long long> resultArray(vector<int>& nums, int k) {
8        vector<long long> ans(k, 0);
9        vector<long long> dp(k, 0);
10
11        for (int num : nums) {
12            vector<long long> next_dp(k, 0);
13            int mod_val = num % k;
14
15            // Start a new subarray ending at current element
16            next_dp[mod_val]++;
17
18            // Extend existing subarrays
19            for (int r = 0; r < k; ++r) {
20                if (dp[r] > 0) {
21                    int new_r = (r * mod_val) % k;
22                    next_dp[new_r] += dp[r];
23                }
24            }
25
26            dp = move(next_dp);
27
28            // Accumulate counts for all remainders ending at current index
29            for (int r = 0; r < k; ++r) {
30                ans[r] += dp[r];
31            }
32        }
33
34        return ans;
35    }
36};
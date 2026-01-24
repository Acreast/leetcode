// Last updated: 1/24/2026, 12:18:43 PM
1import java.lang.Math;
2
3class Solution {
4    public int minPairSum(int[] nums) {
5        Arrays.sort(nums);
6        int n = nums.length;
7        int res = 0;
8        for (int i = 0; i < n/2; ++i ) {
9            res = Math.max(res, (nums[i] + nums[n - i - 1]));
10        }
11        return res;
12    }
13}
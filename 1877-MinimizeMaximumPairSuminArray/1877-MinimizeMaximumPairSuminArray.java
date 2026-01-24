// Last updated: 1/24/2026, 12:20:32 PM
1import java.lang.Math;
2
3class Solution {
4    public int minPairSum(int[] nums) {
5        Arrays.sort(nums);
6        int res = 0;
7        int n = nums.length;
8
9        for (int i = 0; i < n/2; i++) {
10            res = Math.max(res, nums[i] + nums[n - i - 1]);
11        }
12
13        return res;
14    }
15}
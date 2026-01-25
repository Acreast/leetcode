// Last updated: 1/25/2026, 3:27:21 PM
1import java.lang.Math;
2class Solution {
3    public int minimumDifference(int[] nums, int k) {
4        if (nums.length < k) {
5            return 0;
6        }
7        int res = Integer.MAX_VALUE;
8        int j = k - 1;
9        Arrays.sort(nums);
10        for (int i = 0; i + j < nums.length; i ++) {
11            res = Math.min(res, (nums[i + j] - nums[i]));
12        }
13
14        return res;
15    }
16}
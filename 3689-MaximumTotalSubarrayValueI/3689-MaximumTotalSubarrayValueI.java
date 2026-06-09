// Last updated: 6/10/2026, 12:12:27 AM
1class Solution {
2    public long maxTotalValue(int[] nums, int k) {
3        int min = nums[0], max = nums[0];
4
5        for (int n : nums) {
6            min = Math.min(min, n);
7            max = Math.max(max, n);
8        }
9
10        return (long) (max - min) * k;
11    }
12}
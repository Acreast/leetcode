// Last updated: 4/13/2026, 9:20:19 PM
1class Solution {
2    public int getMinDistance(int[] nums, int target, int start) {
3        int res = Integer.MAX_VALUE;
4        for (int i = 0; i < nums.length; i ++) {
5            if (nums[i] == target) {
6                res = Math.min(res, Math.abs(i - start));
7            }
8        }
9
10        return res;
11    }
12}
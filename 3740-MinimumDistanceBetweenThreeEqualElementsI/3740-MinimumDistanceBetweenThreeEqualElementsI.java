// Last updated: 4/11/2026, 12:27:11 AM
1class Solution {
2    public int minimumDistance(int[] nums) {
3        int res = Integer.MAX_VALUE;
4        for (int i = 0; i < nums.length - 2 ; i ++) {
5            for (int j = i + 1; j < nums.length - 1; j ++) {
6                for (int k = j + 1; k < nums.length; k ++) {
7                    if (nums[i] == nums[j] && nums[i] == nums[k]) {
8                        res = Math.min(res, Math.abs(i - j) + Math.abs(j - k) + Math.abs(k - i));
9                    }
10                }
11            }
12        }
13        if (res == Integer.MAX_VALUE) return -1;
14        return res;
15    }
16}
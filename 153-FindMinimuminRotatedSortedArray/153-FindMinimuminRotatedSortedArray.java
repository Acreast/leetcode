// Last updated: 5/15/2026, 11:55:46 PM
1class Solution {
2    public int findMin(int[] nums) {
3        int l = 0;
4        int r = nums.length - 1;
5        int res = nums[0];
6        while (l <= r) {
7            if (nums[l] < nums[r]) {
8                res = Math.min(res, nums[l]);
9                break;
10            }
11            int m = (l + r) / 2;
12            res = Math.min(nums[m], res);
13            if (nums[m] >= nums[l]){
14                l = m + 1;
15            } else {
16                r = m - 1;
17            }
18 
19        }
20
21        return res;
22    }
23}
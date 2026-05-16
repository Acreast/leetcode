// Last updated: 5/16/2026, 11:32:14 PM
1class Solution {
2    public int findMin(int[] nums) {
3        int l = 0;
4        int r = nums.length - 1;
5        int res = nums[0];
6        int last = nums[nums.length - 1];
7        while (l < nums.length && nums[l] == last){
8            l ++;
9        }
10
11        while (l <= r) {
12            if (nums[l] < nums[r]) {
13                res = Math.min(res, nums[l]);
14                break;
15            }
16            int m = (l + r) / 2;
17            res = Math.min(nums[m], res);
18            if (nums[m] >= nums[l]){
19                l = m + 1;
20            } else {
21                r = m - 1;
22            }
23 
24        }
25
26        return res;
27    }
28}
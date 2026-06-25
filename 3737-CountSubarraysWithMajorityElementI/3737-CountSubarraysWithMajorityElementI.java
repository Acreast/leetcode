// Last updated: 6/26/2026, 1:04:17 AM
1class Solution {
2    public int countMajoritySubarrays(int[] nums, int target) {
3        int n = nums.length;
4        int res = 0;
5
6        for (int l = 0; l < n; l ++) {
7            int counter = 0;
8
9            for (int r = l; r < n; r ++) {
10                if (nums[r] == target)
11                    counter ++;
12                
13                int len = r - l + 1;
14
15                if (counter > len / 2)
16                    res ++;
17            }
18
19        }
20
21        return res;
22    }
23}
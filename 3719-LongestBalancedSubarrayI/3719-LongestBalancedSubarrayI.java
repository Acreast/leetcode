// Last updated: 2/10/2026, 11:54:44 PM
1class Solution {
2    public int longestBalanced(int[] nums) {
3        int res = 0;
4
5        for (int i = 0; i < nums.length; i ++) {
6            HashSet<Integer> even = new HashSet<>();
7            HashSet<Integer> odd = new HashSet<>();
8
9            for (int j = i; j < nums.length; j ++) {
10                if (nums[j] % 2 == 0) {
11                    even.add(nums[j]);
12                } else {
13                    odd.add(nums[j]);
14                }
15                if (even.size() == odd.size()) {
16                    res = Math.max(res, j - i + 1);
17                }
18            }
19        }
20
21        return res;
22    }
23}
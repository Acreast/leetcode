// Last updated: 5/23/2026, 4:53:37 PM
1class Solution {
2    public boolean check(int[] nums) {
3        int n = nums.length;
4        int drops = 0;
5        for (int i = 0; i < nums.length; i ++) {
6            if (nums[i] > nums[(i + 1) % n]) {
7                drops += 1;
8            }
9            if (drops > 1) {
10                return false;
11            }
12            
13        }
14
15        return true;
16    }
17}
// Last updated: 3/9/2026, 12:31:05 AM
1class Solution {
2    public String findDifferentBinaryString(String[] nums) {
3        char [] res = new char[nums.length];
4        for (int i = 0; i < nums.length; i ++) {
5            char c = nums[i].charAt(i);
6            res[i] = (c == '0') ? '1' : '0';
7        }
8
9        return new String(res);
10    }
11}
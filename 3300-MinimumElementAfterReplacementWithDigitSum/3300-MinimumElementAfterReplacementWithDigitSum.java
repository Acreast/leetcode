// Last updated: 5/29/2026, 11:13:15 PM
1class Solution {
2    public int minElement(int[] nums) {
3        int smallest = Integer.MAX_VALUE;
4        for (int i = 0; i < nums.length; i ++) {
5            String val = Integer.toString(nums[i]);
6            int num = 0;
7            for (char ch: val.toCharArray()) {
8                num += Character.getNumericValue(ch);
9            }
10            smallest = Math.min(smallest, num);
11        }
12
13        return smallest;
14    }
15}
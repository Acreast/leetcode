// Last updated: 6/6/2026, 8:35:09 PM
1class Solution {
2    public int[] leftRightDifference(int[] nums) {
3        int[] rightSum = new int[nums.length];
4        int[] leftSum = new int[nums.length];
5        int[] res = new int[nums.length];
6
7        int sum = 0;
8        for (int i = 0; i < nums.length; i ++) {
9            sum += nums[i];
10            leftSum[i] = sum;
11        }
12        sum = 0;
13        for (int i = nums.length - 1; i >= 0; i --) {
14            sum += nums[i];
15            rightSum[i] = sum;
16        }
17
18        for (int i = 0; i < nums.length; i ++) {
19            res[i] = Math.abs(leftSum[i] - rightSum[i]);
20        }
21
22        return res;
23    }
24}
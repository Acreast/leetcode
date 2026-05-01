// Last updated: 5/1/2026, 11:49:51 PM
1class Solution {
2    public int maxRotateFunction(int[] nums) {
3        int sum = 0, F = 0;
4        int n = nums.length;
5
6        for (int i = 0; i < n; i ++) {
7            sum += nums[i];
8            F += i * nums[i];
9        }
10
11        int max = F;
12
13        for (int i = 1; i < n; i ++) {
14            F += sum - n * nums[n - i];
15            max = Math.max(max, F);
16        }
17
18        return max;
19    }
20}
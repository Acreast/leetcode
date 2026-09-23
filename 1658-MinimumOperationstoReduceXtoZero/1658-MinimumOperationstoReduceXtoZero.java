// Last updated: 9/23/2026, 11:21:04 PM
1class Solution {
2    public int minOperations(int[] nums, int x) {
3        int target = -x;
4        for (int num : nums) target += num;
5
6        if (target == 0) return nums.length;  // since all elements are positive, we have to take all of them
7
8        Map<Integer, Integer> map = new HashMap<>();
9        map.put(0, -1);
10        int sum = 0;
11        int res = Integer.MIN_VALUE;
12
13        for (int i = 0; i < nums.length; ++i) {
14
15            sum += nums[i];
16            if (map.containsKey(sum - target)) {
17                res = Math.max(res, i - map.get(sum - target));
18            }
19
20            // no need to check containsKey since sum is unique
21            map.put(sum, i);
22        }
23
24        return res == Integer.MIN_VALUE ? -1 : nums.length - res;
25    }
26}
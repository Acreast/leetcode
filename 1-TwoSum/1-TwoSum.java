// Last updated: 1/24/2026, 4:00:52 PM
1class Solution {
2    public int[] twoSum(int[] nums, int target) {
3        Map<Integer, Integer> map = new HashMap<>();
4
5        for (int i = 0; i < nums.length; i ++) {
6            int delta = target - nums[i];
7
8            if (map.containsKey(delta)) {
9                return new int[] {map.get(delta), i};
10            }
11
12            map.put(nums[i],i);
13        }
14
15        return new int[0]; 
16    }
17}
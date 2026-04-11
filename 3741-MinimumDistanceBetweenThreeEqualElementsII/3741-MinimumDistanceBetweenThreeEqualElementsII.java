// Last updated: 4/11/2026, 11:37:51 PM
1class Solution {
2    public int minimumDistance(int[] nums) {
3        int n = nums.length;
4        Map<Integer, List<Integer>> map = new HashMap<>();
5
6        for (int i = 0; i < n; i ++) {
7            map.putIfAbsent(nums[i], new ArrayList<>());
8            map.get(nums[i]).add(i);
9        }
10
11        int minDistance = Integer.MAX_VALUE;
12
13        for (List<Integer> indices: map.values()) {
14            if (indices.size() >= 3) {
15                for (int idx = 0; idx < indices.size() - 2; idx ++) {
16                    int i = indices.get(idx);
17                    int k = indices.get(idx + 2);
18                    int distance = 2 * (k - i);
19
20                    minDistance = Math.min(minDistance, distance);
21                }
22            }
23        }
24
25        return minDistance == Integer.MAX_VALUE ? -1 : minDistance;
26    }
27}
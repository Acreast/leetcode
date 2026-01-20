// Last updated: 1/21/2026, 12:20:33 AM
1class Solution {
2    public int[] minBitwiseArray(List<Integer> nums) {
3        int[] res = new int[nums.size()];
4        Arrays.fill(res, -1);
5        for (int i = 0; i < nums.size(); i ++) {
6            int ptr = 1;
7            int cur = nums.get(i);
8            while (ptr < cur) {
9
10                if ((ptr | ptr + 1) == cur) {
11                    res[i] = ptr;
12                    break;
13                }
14                ptr += 1;
15            }
16        }
17
18        return res;
19    }
20}
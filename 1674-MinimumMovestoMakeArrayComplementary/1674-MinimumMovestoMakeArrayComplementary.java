// Last updated: 5/14/2026, 12:24:10 AM
1class Solution {
2    public int minMoves(int[] nums, int limit) {
3        int n = nums.length;
4        int[] delta = new int[(limit << 1) + 2 ];
5
6        for ( int i = 0; i < n >> 1; i ++) {
7            int min = Math.min(nums[i], nums[n - 1- i]);
8            int max = Math.max(nums[i], nums[n - 1- i]);
9
10            delta[2] += 2;
11            delta[min + 1] --;
12            delta[min + max] --;
13            delta[min + max + 1]++;
14            delta[max + limit + 1]++;
15        }
16
17
18        int res = n, moves = 0;
19
20        for (int targ = 2; targ <= limit * 2; targ ++) {
21            moves += delta[targ];
22            res = Math.min(res, moves);
23        }
24        return res;
25    }
26}
// Last updated: 6/28/2026, 1:39:56 AM
1class Solution {
2    public int maximumLength(int[] nums) {
3        Map<Integer, Integer> freq = new HashMap<>();
4        for (int n: nums)
5            freq.merge(n, 1, Integer::sum);
6        
7        int one = freq.getOrDefault(1, 0);
8        int res = (one - 1) | 1;
9        freq.remove(1);
10
11        for (int f: freq.keySet()) {
12            int sq = (int) Math.sqrt(f);
13            if (sq * sq == f && freq.getOrDefault(sq, 0) > 1)
14                continue;
15            
16            int n = 0, x = f;
17
18            while (x < 31623 && freq.containsKey(x) && freq.get(x) > 1) {
19                n += 2;
20                x *= x;
21            }
22
23            res = Math.max(res, n + (freq.containsKey(x) ? 1 : -1));
24        }
25        return res;
26    }
27}
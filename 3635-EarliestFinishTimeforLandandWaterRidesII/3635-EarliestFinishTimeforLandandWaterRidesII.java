// Last updated: 6/4/2026, 12:00:22 AM
1class Solution {
2    public int earliestFinishTime(int[] startL, int[] durL, int[] startW, int[] durW) {
3        int minL = 300005, minW = minL, res = minW;
4        int n = startL.length;
5        int m = startW.length;
6
7        for (int i = 0; i < n; i++)
8            minL = Math.min(minL, startL[i] + durL[i]);
9
10        for (int i = 0; i < m; i++) {
11            minW = Math.min(minW, startW[i] + durW[i]);
12            res = Math.min(res, Math.max(minL, startW[i]) + durW[i]);
13        }
14
15        for (int i = 0; i < n; i++)
16            res = Math.min(res, Math.max(minW, startL[i]) + durL[i]);
17
18        return res;
19    }
20}
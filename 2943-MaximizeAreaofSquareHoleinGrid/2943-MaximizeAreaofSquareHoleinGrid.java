// Last updated: 1/15/2026, 10:27:02 PM
1class Solution {
2    public int maximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {
3        Arrays.sort(hBars);
4        Arrays.sort(vBars);
5        int s = Math.min(maxSpan(hBars), maxSpan(vBars));
6        return s * s;
7    }
8
9    private int maxSpan(int[] bars) {
10        int res = 1, streak = 1;
11
12        for(int i = 1; i < bars.length; i ++) {
13            if (bars[i] - bars[i-1] == 1) streak++;
14            else streak = 1;
15            res = Math.max(res, streak);
16        }
17        return ++ res;
18    }
19
20}
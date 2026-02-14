// Last updated: 2/15/2026, 1:34:09 AM
1class Solution {
2    public double champagneTower(int poured, int query_row, int query_glass) {
3
4        double[] prev_row = new double[1];
5        prev_row[0] = poured;
6
7        for (int row = 1; row <= query_row; row++) {
8
9            double[] cur_row = new double[row + 1];
10
11            for (int i = 0; i < prev_row.length; i++) {
12                double extra = prev_row[i] - 1.0;
13
14                if (extra > 0) {
15                    cur_row[i] += extra / 2.0;
16                    cur_row[i + 1] += extra / 2.0;
17                }
18            }
19
20            prev_row = cur_row; // move to next row AFTER finishing
21        }
22
23        return Math.min(1.0, prev_row[query_glass]);
24    }
25}
26
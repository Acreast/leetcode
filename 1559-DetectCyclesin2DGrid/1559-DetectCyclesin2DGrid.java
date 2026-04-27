// Last updated: 4/28/2026, 12:12:30 AM
1class Solution {
2    private static final int[][] TRANS = {
3        {-1, 1, -1, 3},
4        {0, -1, 2, -1},
5        {3, 2, -1, -1},
6        {1, -1, -1, 2},
7        {-1, 0, 3, -1},
8        {-1, -1, 1, 0}
9    };
10    private static final int[][] DIRS = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
11    private static final int[][] START = {{1, 3}, {0, 2}, {2, 3},
12                                          {1, 2}, {0, 3}, {0, 1}};
13
14    public boolean hasValidPath(int[][] grid) {
15        int m = grid.length, n = grid[0].length;
16        if (m == 1 && n == 1) return true;
17
18        int[] s = START[grid[0][0] - 1];
19        return check(grid, s[0]) || check(grid, s[1]);
20    }
21
22    private boolean check(int[][] grid, int di) {
23        if (di == -1) return false;
24        int m = grid.length, n = grid[0].length;
25        int r = DIRS[di][0];
26        int c = DIRS[di][1];
27
28        while (r >= 0 && r < m && c >= 0 && c < n) {
29            di = TRANS[grid[r][c] - 1][di];
30            if (di == -1 || r == 0 && c == 0) return false;
31            if (r == m - 1 && c == n - 1) return true;
32
33            r += DIRS[di][0];
34            c += DIRS[di][1];
35        }
36        return false;
37    }
38}
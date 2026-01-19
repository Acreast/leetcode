// Last updated: 1/20/2026, 12:15:41 AM
1class Solution {
2    public int maxSideLength(int[][] mat, int threshold) {
3        int ROWS = mat.length;
4        int COLS = mat[0].length;
5        int res = 0;
6
7        int[][] prefix = new int[ROWS + 1][COLS + 1];
8
9        for (int i = 1; i <= ROWS; i++) {
10            for (int j = 1; j <= COLS; j++) {
11                prefix[i][j] = mat[i - 1][j - 1]
12                + prefix[i - 1][j]
13                + prefix[i][j - 1]
14                - prefix[i - 1][j - 1];
15            }
16        }
17
18        int l = 0;
19        int r = Math.min(ROWS,COLS);
20
21        while (l <= r) {
22            int mid = l + (r - l) / 2;
23
24            if (is_valid_square(prefix, mid, ROWS, COLS, threshold)) {
25                res = mid;
26                l = mid + 1;
27            } else {
28                r = mid - 1;
29            }
30        }
31
32        return res;
33
34    }
35
36    public boolean is_valid_square(int[][] prefix, int k, int ROWS, int COLS, int threshold) {
37        if (k == 0) return true;
38
39        for (int i = 0; i <= ROWS - k; i ++) {
40            for (int j = 0; j <= COLS - k; j ++) {
41                int sum = prefix[i + k][j + k]
42                - prefix[i + k][j]
43                - prefix[i][j + k]
44                + prefix[i][j];
45
46                if (sum <= threshold) return true;
47            } 
48        }
49        return false;
50    }
51}
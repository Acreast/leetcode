// Last updated: 5/4/2026, 11:17:38 PM
1class Solution {
2    public void rotate(int[][] mat) {
3        int m = mat.length;
4        int k = m - 1;
5
6        for (int i = 0; i < m >> 1; i ++) {
7            for (int j = i; j < k - i; j ++) {
8                int curr = mat[i][j];
9                mat[i][j] = mat[k - j][i];
10                mat[k - j][i] = mat[k - i][k - j];
11                mat[k - i][k - j] = mat[j][k - i];
12                mat[j][k - i] = curr;
13            }
14        }
15    }
16}
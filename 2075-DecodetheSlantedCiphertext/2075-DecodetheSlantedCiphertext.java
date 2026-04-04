// Last updated: 4/5/2026, 12:00:56 AM
1class Solution {
2    public String decodeCiphertext(String s, int r) {
3        if (r == 1) return s;
4        int n = s.length();
5
6        int c = (int)Math.ceil((double) n / r);
7
8        char[][] mat = new char[r][c];
9        char[] arr = s.toCharArray();
10        int p = 0;
11
12        for (int i = 0; i < r; i ++) {
13            for (int j = 0; j < c; j ++) {
14                mat[i][j] = arr[p++];
15            }
16        }
17
18        StringBuilder res = new StringBuilder();
19        for (int k = 0; k < c; k ++) {
20            int x = 0, y = k;
21            while (x < r && y < c) {
22                res.append(mat[x][y]);
23                x ++;
24                y ++;
25            }
26        }
27
28        return res.toString().stripTrailing();
29    }
30}
// Last updated: 5/6/2026, 11:31:06 PM
1class Solution {
2    public char[][] rotateTheBox(char[][] grid) {
3        int rows = grid.length;
4        int cols = grid[0].length;
5
6        for (int r = 0; r < rows; r ++) {
7            int p = 0;
8            for (int c = 0 ; c < cols; c ++) {
9                if (grid[r][c] == '.') {
10                    char temp = grid[r][c];
11                    grid[r][c] = grid[r][p];
12                    grid[r][p] = temp;
13                    p ++;
14                } else if (grid[r][c] == '*') {
15                    p = c + 1;
16                }
17            }
18        }
19
20        char[][] res = new char[cols][rows];
21        for (int r = 0; r < rows; r ++) {
22            for (int c = 0; c < cols; c ++) {
23                res[c][rows - 1 - r] = grid[r][c];
24            }
25        }
26        return res;
27    }
28}
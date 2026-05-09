// Last updated: 5/9/2026, 9:52:54 PM
1class Solution {
2    public int[][] rotateGrid(int[][] grid, int k) {
3        int T = 0;
4        int B = grid.length - 1;
5        int L = 0;
6        int R = grid[0].length - 1;
7
8        while (T < B && L < R) {
9            int len = B - T;
10            int wid = R - L;
11            int peri = 2 * len + 2 * wid;
12            // Reduce operations
13            int r = k % peri;
14
15            while (r -- > 0) {
16                int temp = grid[T][L];
17
18                for (int i = L; i < R; i ++) 
19                    grid[T][i] = grid[T][i + 1];
20
21                for (int i = T; i < B; i ++) 
22                    grid[i][R] = grid[i + 1][R];
23
24                for (int i = R; i > L; i --) 
25                    grid[B][i] = grid[B][i - 1];
26
27                for (int i = B; i > T; i --) 
28                    grid[i][L] = grid[i - 1][L];
29                
30                grid[T + 1][L] = temp;
31            }
32
33            T ++;
34            L ++;
35            R --;
36            B --;
37        }
38        return grid;
39    }
40}
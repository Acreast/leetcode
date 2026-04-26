// Last updated: 4/27/2026, 1:04:42 AM
1class Solution {
2    static int[][] dirs ={{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
3    public boolean containsCycle(char[][] grid) {
4        int m = grid.length;
5        int n = grid[0].length;
6        boolean[] visit = new boolean[m * n];
7
8        for (int i = 0; i < m; i ++)
9            for (int j = 0; j < n; j ++)
10                if (!visit[i * n + j] && dfs(i, j, - 1, -1, grid, visit, m, n))
11                    return true;
12        return false;
13    }
14
15    private static boolean dfs(int r, int c, int pr, int pc, char[][] grid, boolean[] visit, int m, int n) {
16        visit[r * n + c] = true;
17        for(int[] d : dirs) {
18            int nr = r + d[0];
19            int nc = c + d[1];
20            if (nr != pr || nc != pc)
21                if (nr >= 0 && nr < m && nc >= 0 && nc < n)
22                    if (grid[nr][nc] == grid[r][c])
23                        if (visit[nr * n + nc] || dfs(nr, nc, r,c, grid,visit,m,n))
24                            return true;
25        }
26        return false;
27    }
28}
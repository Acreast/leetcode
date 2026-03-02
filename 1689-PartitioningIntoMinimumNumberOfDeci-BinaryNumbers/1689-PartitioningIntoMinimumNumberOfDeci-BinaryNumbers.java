// Last updated: 3/3/2026, 12:01:04 AM
1class Solution {
2    public int minSwaps(int[][] grid) {
3        int n = grid.length;
4        int[] zeros = new int[n];
5
6        for (int i = 0; i < n; i++) {
7            int count = 0;
8            for (int j = n - 1; j >= 0; j--) {
9                if (grid[i][j] == 0) {
10                    count++;
11                } else {
12                    break;
13                }
14            }
15            zeros[i] = count;
16        }
17
18        int swaps = 0;
19        for (int i = 0; i < n; i++) {
20            int need = n - 1 - i;
21
22            int found = -1;
23            for (int j = i; j < n; j++) {
24                if (zeros[j] >= need) {
25                    found = j;
26                    break;
27                } 
28            }
29
30            if (found == -1) return -1;
31
32            for (int j = found; j > i; j--) {
33                int temp = zeros[j];
34                zeros[j] = zeros[j - 1];
35                zeros[j - 1] = temp;
36                swaps++;
37            }
38        }
39
40        return swaps;
41    }
42}
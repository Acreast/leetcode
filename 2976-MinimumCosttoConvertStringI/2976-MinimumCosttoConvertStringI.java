// Last updated: 1/30/2026, 1:01:02 AM
1import java.util.Arrays;
2
3class Solution {
4    public long minimumCost(String source, String target, 
5char[] original, char[] changed, int[] cost) {
6        long[][] dist = new long[26][26];
7        long INF = Long.MAX_VALUE / 2;
8
9        for (long[] row : dist) {
10            Arrays.fill(row, INF);
11        }
12        for (int i = 0; i < 26; i++) {
13            dist[i][i] = 0;
14        }
15
16        for (int i = 0; i < original.length; i++) {
17            int u = original[i] - 'a';
18            int v = changed[i] - 'a';
19            dist[u][v] = Math.min(dist[u][v], cost[i]);
20        }
21
22        for (int k = 0; k < 26; k++) {
23            for (int i = 0; i < 26; i++) {
24                if (dist[i][k] == INF) continue;
25                for (int j = 0; j < 26; j++) {
26                    if (dist[k][j] != INF) {
27                        dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
28                    }
29                }
30            }
31        }
32
33        long totalCost = 0;
34        int n = source.length();
35
36        for (int i = 0; i < n; i++) {
37            int u = source.charAt(i) - 'a';
38            int v = target.charAt(i) - 'a';
39            if (u == v) continue;
40            if (dist[u][v] == INF) return -1;
41            totalCost += dist[u][v];
42        }
43
44        return totalCost;
45    }
46}
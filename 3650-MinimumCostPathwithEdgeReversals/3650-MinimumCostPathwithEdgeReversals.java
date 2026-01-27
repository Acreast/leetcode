// Last updated: 1/28/2026, 12:44:51 AM
1import java.util.*;
2
3class Solution {
4    public int minCost(int n, int[][] edges) {
5        List<List<int[]>> out = new ArrayList<>();
6        List<List<int[]>> in = new ArrayList<>();
7        for (int i = 0; i < n; i++) {
8            out.add(new ArrayList<>());
9            in.add(new ArrayList<>());
10        }
11
12        for (int[] e : edges) {
13            out.get(e[0]).add(new int[]{e[1], e[2]});
14            in.get(e[1]).add(new int[]{e[0], e[2]});
15        }
16
17        long INF = (long) 1e18;
18        long[][] dist = new long[n][2];
19        for (int i = 0; i < n; i++) {
20            Arrays.fill(dist[i], INF);
21        }
22
23        PriorityQueue<long[]> pq =
24            new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));
25        dist[0][0] = 0;
26        pq.add(new long[]{0, 0, 0}); // cost, node, used
27
28        while (!pq.isEmpty()) {
29            long[] cur = pq.poll();
30            long cost = cur[0];
31            int u = (int) cur[1];
32            int used = (int) cur[2];
33
34            if (cost > dist[u][used]) continue;
35
36            // Normal edges
37            for (int[] edge : out.get(u)) {
38                int v = edge[0];
39                int w = edge[1];
40                if (dist[v][0] > cost + w) {
41                    dist[v][0] = cost + w;
42                    pq.add(new long[]{dist[v][0], v, 0});
43                }
44            }
45
46            // Reversed edges (only if switch unused)
47            if (used == 0) {
48                for (int[] edge : in.get(u)) {
49                    int v = edge[0];
50                    int w = edge[1];
51                    if (dist[v][0] > cost + 2L * w) {
52                        dist[v][0] = cost + 2L * w;
53                        pq.add(new long[]{dist[v][0], v, 0});
54                    }
55                }
56            }
57        }
58
59        long ans = Math.min(dist[n - 1][0], dist[n - 1][1]);
60        return ans >= INF ? -1 : (int) ans;
61    }
62}
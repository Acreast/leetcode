// Last updated: 7/4/2026, 1:25:56 AM
1class Solution {
2    private boolean check(long mid, List<int[]>[] adj, List<Integer> topo,
3                          boolean[] online, long k, int n) {
4
5        long INF = (long) 1e18;
6        long[] dist = new long[n];
7        Arrays.fill(dist, INF);
8        dist[0] = 0;
9
10        for (int u : topo) {
11            if (dist[u] == INF) continue;
12
13            if (u != 0 && u != n - 1 && !online[u]) continue;
14
15            for (int[] edge : adj[u]) {
16                int v = edge[0];
17                int w = edge[1];
18
19                if (w < mid) continue;
20                if (v != n - 1 && !online[v]) continue;
21
22                dist[v] = Math.min(dist[v], dist[u] + w);
23            }
24        }
25
26        return dist[n - 1] <= k;
27    }
28
29    public int findMaxPathScore(int[][] edges, boolean[] online, long k) {
30
31        int n = online.length;
32
33        List<int[]>[] adj = new ArrayList[n];
34        for (int i = 0; i < n; i++)
35            adj[i] = new ArrayList<>();
36
37        int[] indegree = new int[n];
38
39        int maxEdge = 0;
40
41        for (int[] e : edges) {
42            int u = e[0];
43            int v = e[1];
44            int w = e[2];
45
46            adj[u].add(new int[]{v, w});
47            indegree[v]++;
48            maxEdge = Math.max(maxEdge, w);
49        }
50
51        Queue<Integer> q = new LinkedList<>();
52
53        for (int i = 0; i < n; i++) {
54            if (indegree[i] == 0)
55                q.offer(i);
56        }
57
58        List<Integer> topo = new ArrayList<>();
59
60        while (!q.isEmpty()) {
61            int u = q.poll();
62            topo.add(u);
63
64            for (int[] edge : adj[u]) {
65                int v = edge[0];
66                indegree[v]--;
67
68                if (indegree[v] == 0)
69                    q.offer(v);
70            }
71        }
72
73        long low = 0, high = maxEdge;
74        int ans = -1;
75
76        while (low <= high) {
77            long mid = low + (high - low) / 2;
78
79            if (check(mid, adj, topo, online, k, n)) {
80                ans = (int) mid;
81                low = mid + 1;
82            } else {
83                high = mid - 1;
84            }
85        }
86
87        return ans;
88    }
89}
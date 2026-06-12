// Last updated: 6/13/2026, 12:19:24 AM
1class Solution {
2    static int[] binaryExponent;
3    static final long mod = 1000000007l;
4
5    static {
6        binaryExponent = new int[100001];
7        long pro = 1l;
8        for (int i = 1; i < binaryExponent.length; i++) {
9            binaryExponent[i] = (int) (pro);
10            pro = (pro * 2l) % mod;
11        }
12    }
13    
14    int[][] ancestors;
15    int[] ans, parent;
16    int[] depth;
17    boolean[] visited;
18
19    private void buildAncestors(int[] parent, int numNodes) {
20        ancestors = new int[(int) (Math.log(numNodes) / Math.log(2)) + 1][numNodes + 1];
21        int n = ancestors.length, m = ancestors[0].length;
22        for (int i = 0; i < m; i++) {
23            ancestors[0][i] = parent[i];
24        }
25
26        for (int i = 1; i < n; i++) {
27            for (int j = 1; j < m; j++) {
28                ancestors[i][j] = ancestors[i - 1][ancestors[i - 1][j]];
29            }
30        }
31    }
32
33    public int[] assignEdgeWeights(int[][] edges, int[][] queries) {
34        int n = edges.length, q = queries.length;
35        ans = new int[q];
36        parent = new int[n + 2];
37        visited = new boolean[n + 2];
38        depth = new int[n + 2];
39
40        List<List<Integer>> adj = new ArrayList<>();
41        for (int i = 0; i <= n + 1; i++) {
42            adj.add(new ArrayList<>());
43        }
44        for (int i = 0; i < edges.length; i++) {
45            adj.get(edges[i][0]).add(edges[i][1]);
46            adj.get(edges[i][1]).add(edges[i][0]);
47        }
48
49        parent[1] = 1;
50
51        dfs(1, adj, 0);
52        buildAncestors(parent, n + 1);
53        
54        for (int i = 0; i < q; i++) {
55            ans[i] = binaryExponent[getPathCount(queries[i][0], queries[i][1])];
56        }
57        return ans;
58    }
59
60    private int getPathCount(int u, int v) {
61        int depthU = depth[u], depthV = depth[v], lca = -1;
62
63        if (depthU > depthV) lca = LCA(u, v);
64        else lca = LCA(v, u);
65    
66        return depth[u] + depth[v] - 2 * depth[lca];
67    }
68
69    private int LCA(int u, int v) {
70        int depthU = depth[u];
71        int depthV = depth[v];
72
73        int diff = depthU - depthV;
74        int mask = 1, idx = 0;
75
76        while (mask <= diff) {
77            if ((mask & diff) > 0) {
78                u = ancestors[idx][u];
79            }
80
81            mask <<= 1;
82            idx++;
83        }
84
85        if (u == v) return u;
86
87        int maxJumps = ancestors.length - 1;
88
89        while (maxJumps >= 0) {
90            if (ancestors[maxJumps][u] != ancestors[maxJumps][v]) {
91                u = ancestors[maxJumps][u];
92                v = ancestors[maxJumps][v];
93            }
94            maxJumps--;
95        }
96
97        int lca = ancestors[0][u];
98        return lca;
99    }
100
101    private void dfs(int node, List<List<Integer>> adj, int depthValue) {
102        visited[node] = true;
103        depth[node] = depthValue;
104        List<Integer> children = adj.get(node);
105
106        for (int v : children) {
107            if (visited[v]) continue;
108            parent[v] = node;
109            dfs(v, adj, depthValue + 1);
110        }
111    }
112
113}
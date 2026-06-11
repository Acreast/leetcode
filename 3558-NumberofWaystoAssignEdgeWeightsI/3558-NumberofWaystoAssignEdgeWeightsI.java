// Last updated: 6/12/2026, 12:39:26 AM
1class Solution {
2    private static final int mod = 1_000_000_007;
3
4    public int assignEdgeWeights(int[][] edges) {
5        int n = edges.length + 1;
6        List<Integer>[] graph = new ArrayList[n + 1];
7        Arrays.setAll(graph, i -> new ArrayList<>());
8        
9        for (int[] e : edges) {
10            graph[e[0]].add(e[1]);
11            graph[e[1]].add(e[0]);
12        }
13
14        return (int) pow(2, dfs(1, 0, graph) - 1);
15    }
16
17    private int dfs(int node, int prev, List<Integer>[] graph) {
18        int dist = 0;
19        for (int g : graph[node])
20            if (g != prev)
21                dist = Math.max(dist, dfs(g, node, graph) + 1);
22        return dist;
23    }
24
25    private long pow(long base, int exp) {
26        long res = 1;
27        while (exp > 0) {
28            if (exp % 2 > 0)
29                res = res * base % mod;
30            base = base * base % mod;
31            exp /= 2;
32        }
33        return res;
34    }
35}
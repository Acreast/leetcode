// Last updated: 3/13/2026, 12:10:18 AM
1class Solution {
2    class Edge {
3        int u, v, strength;
4        boolean must;
5        
6        Edge(int u, int v, int strength, boolean must) {
7            this.u = u;
8            this.v = v;
9            this.strength = strength;
10            this.must = must;
11        }
12    }
13    
14    class DSU {
15        int[] parent, rank;
16
17        DSU(int n) {
18            parent = new int[n];
19            rank = new int[n];
20
21            for (int i = 0; i < n; i++) {
22                parent[i] = i;
23            }
24        }
25
26        int find(int x) {
27            if (parent[x] != x) {
28                parent[x] = find(parent[x]);
29            }
30            return parent[x];  
31        }
32
33        void union(int x, int y) {
34            int root_x = find(x), root_y = find(y);
35            
36            if (root_x == root_y) return;
37
38            if (rank[root_x] < rank[root_y]) {
39                parent[root_x] = root_y;
40            } else if (rank[root_x] > rank[root_y]) {
41                parent[root_y] = root_x;
42            } else {
43                parent[root_y] = root_x;
44                rank[root_x]++;
45            }
46        }
47    }
48
49    public int maxStability(int n, int[][] edges, int k) {
50        List<Edge> mandatory = new ArrayList<>();
51        List<Edge> optional = new ArrayList<>();
52        
53        for (int[] e : edges) {	
54            Edge edge = new Edge(e[0], e[1], e[2], e[3] == 1);
55            if (edge.must) {
56                mandatory.add(edge);
57            } else {
58                optional.add(edge);
59            }
60        }
61    
62        DSU dsu = new DSU(n);
63        
64        for (Edge e : mandatory) {
65            if (dsu.find(e.u) == dsu.find(e.v)) {
66                return -1;
67            }
68            dsu.union(e.u, e.v);
69        }
70        
71        int[] parent_snap = new int[n];
72        int[] rank_snap = new int[n];
73        for (int i = 0; i < n; i++) {
74            parent_snap[i] = dsu.parent[i];
75            rank_snap[i] = dsu.rank[i];
76        }
77        
78        int left = 1;
79        int right = 0;
80        for (int[] e : edges) {
81            right = Math.max(right, e[2] * 2);
82        }
83
84        int answer = -1;
85        
86        while (left <= right) {
87            int mid = left + (right - left) / 2;
88            
89            if (canAchieve(n, mandatory, optional, k, mid, parent_snap, rank_snap)) {
90                answer = mid;
91                left = mid + 1;
92            } else {
93                right = mid - 1;
94            }
95        }
96
97        return answer;
98    }
99
100    private boolean canAchieve(int n, List<Edge> mandatory, List<Edge> optional, 
101                               int k, int minStability, int[] parent_snap, int[] rank_snap) {
102        DSU dsu = new DSU(n);
103        dsu.parent = parent_snap.clone();
104        dsu.rank = rank_snap.clone();
105
106        for (Edge e : mandatory) {
107            if (e.strength < minStability) {
108                return false;
109            }
110        }
111
112        List<Edge> goodWithUpgrade = new ArrayList<>();
113        List<Edge> goodWithoutUpgrade = new ArrayList<>();
114
115        for (Edge e : optional) {
116            if (e.strength >= minStability) {
117                goodWithoutUpgrade.add(e);
118            } else if (e.strength * 2 >= minStability) {
119                goodWithUpgrade.add(e);
120            }
121        }
122
123        for (Edge e : goodWithoutUpgrade) {
124            if (dsu.find(e.u) != dsu.find(e.v)) {
125                dsu.union(e.u, e.v);
126            }
127        }
128        
129        int used = 0;
130        for (Edge e : goodWithUpgrade) {
131            if (used >= k) break;
132            
133            if (dsu.find(e.u) != dsu.find(e.v)) {
134                dsu.union(e.u, e.v);
135                used++;
136            }
137        }
138        
139        int root = dsu.find(0);
140        for (int i = 1; i < n; i++) {
141            if (dsu.find(i) != root) return false;
142        }
143        
144        return true;
145    }
146}
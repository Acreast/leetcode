// Last updated: 5/19/2026, 12:37:55 AM
1class Solution {
2    public int minJumps(int[] arr) {
3        int n = arr.length;
4        if (n == 1) return 0;
5        Map<Integer, List<Integer>> mp = new HashMap<>();
6        for(int i = 0; i < n; i ++) {
7            mp.computeIfAbsent(arr[i], k -> new ArrayList<>()).add(i);
8        }
9
10        Queue<int[]> q = new LinkedList<>();
11        q.offer(new int[]{0, 0});
12
13        boolean[] vis = new boolean[n];
14        vis[0] = true;
15
16        while (!q.isEmpty()) {
17            int[] curr = q.poll();
18            int node = curr[0];
19            int dist = curr[1];
20
21            if (node == n - 1) return dist;
22
23            if (node - 1 >= 0 && !vis[node - 1]) {
24                vis[node - 1] = true;
25                q.offer(new int[]{node - 1, dist + 1});
26            }
27
28            if (node + 1 >= 0 && !vis[node + 1]) {
29                vis[node + 1] = true;
30                q.offer(new int[]{node + 1, dist + 1});
31            }
32
33            for (int next :mp.get(arr[node])) {
34                if (!vis[next]) {
35                    vis[next] = true;
36                    q.offer(new int[]{next, dist + 1});
37                }
38            }
39            mp.get(arr[node]).clear();
40        }
41
42        return - 1;
43    }
44}
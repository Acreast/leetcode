// Last updated: 7/5/2026, 1:00:50 AM
1class Solution {
2    int find(int[] root, int i) {
3        if (root[i] == i)
4            return i;
5        return root[i] = find(root, root[i]);
6    }
7
8    public int minScore(int n, int[][] roads) {
9        int[] root = new int[n + 1];
10        for (int i = 0; i <= n; i++)
11            root[i] = i;
12
13        for (int[] r : roads)
14            root[find(root, r[0])] = find(root, r[1]);
15
16        int res = 10001;
17        for (int[] r : roads)
18            if (find(root, r[0]) == find(root, 1))
19                res = Math.min(res, r[2]);
20
21        return res;
22    }
23}
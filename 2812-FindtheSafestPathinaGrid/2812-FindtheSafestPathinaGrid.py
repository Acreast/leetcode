# Last updated: 7/2/2026, 1:00:01 AM
1class Solution:
2    def __init__(self):
3        self.roww = [0, 0, -1, 1]
4        self.coll = [-1, 1, 0, 0]
5
6    def bfs(self, grid, score, n):
7        q = deque()
8
9        for i in range(n):
10            for j in range(n):
11                if grid[i][j]:
12                    score[i][j] = 0
13                    q.append((i, j))
14
15        while q:
16            x, y = q.popleft()
17            s = score[x][y]
18
19            for i in range(4):
20                new_x = x + self.roww[i]
21                new_y = y + self.coll[i]
22
23                if 0 <= new_x < n and 0 <= new_y < n and score[new_x][new_y] > s + 1:
24                    score[new_x][new_y] = s + 1
25                    q.append((new_x, new_y))
26
27    def maximumSafenessFactor(self, grid):
28        n = len(grid)
29        if grid[0][0] or grid[n - 1][n - 1]:
30            return 0
31
32        score = [[float('inf')] * n for _ in range(n)]
33        self.bfs(grid, score, n)
34
35        vis = [[False] * n for _ in range(n)]
36        pq = [(-score[0][0], 0, 0)]
37        heapq.heapify(pq)
38
39        while pq:
40            safe, x, y = heapq.heappop(pq)
41            safe = -safe
42
43            if x == n - 1 and y == n - 1:
44                return safe
45
46            vis[x][y] = True
47
48            for i in range(4):
49                new_x = x + self.roww[i]
50                new_y = y + self.coll[i]
51
52                if 0 <= new_x < n and 0 <= new_y < n and not vis[new_x][new_y]:
53                    s = min(safe, score[new_x][new_y])
54                    heapq.heappush(pq, (-s, new_x, new_y))
55                    vis[new_x][new_y] = True
56
57        return -1
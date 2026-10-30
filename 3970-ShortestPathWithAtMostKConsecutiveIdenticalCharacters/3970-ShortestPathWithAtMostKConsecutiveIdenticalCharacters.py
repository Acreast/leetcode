# Last updated: 10/30/2026, 11:31:09 PM
1class Solution:
2    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
3        graph = [[] for _ in range(n)]
4        for u, v, w in edges:
5            graph[u].append((v, w))
6
7        best = [k + 1] * n  # best[x]: the shortest run x was settled with, k + 1 until then
8        heap = [(0, 1, 0)]  # (distance, run, node): the walk ends with run nodes labeled labels[node]
9        while heap:
10            d, run, x = heappop(heap)
11            if run >= best[x]:  # x was settled before, no farther away and with a run no longer
12                continue
13            if x == n - 1:
14                return d
15            best[x] = run
16            for y, w in graph[x]:
17                r = run + 1 if labels[y] == labels[x] else 1
18                if r < best[y]:
19                    heappush(heap, (d + w, r, y))
20        return -1
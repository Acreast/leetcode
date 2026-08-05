# Last updated: 8/6/2026, 12:31:49 AM
1class Solution:
2    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
3        edges = [[] for _ in range(n)]
4        in_degree = [0] * n
5
6        for u, v in invocations:
7            edges[u].append(v)
8            in_degree[v] += 1
9
10        queue = collections.deque([k])
11        sus = bytearray(n)
12        sus[k] = 1
13
14        while queue:
15            u = queue.popleft()
16            for v in edges[u]:
17                in_degree[v] -= 1
18
19                if sus[v] == 0:
20                    queue.append(v)
21                    sus[v] = 1
22
23        can_remove_all = True
24        for i in range(n):
25            if sus[i] == 1 and in_degree[i] > 0:
26                can_remove_all = False
27                break
28
29        if not can_remove_all:
30            return list(range(n))
31
32        return [i for i in range(n) if sus[i] == 0]
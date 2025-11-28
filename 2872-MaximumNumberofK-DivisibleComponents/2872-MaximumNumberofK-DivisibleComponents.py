# Last updated: 11/28/2025, 8:59:45 PM
1class Solution:
2    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
3        adj_list = defaultdict(list)
4
5        for n1, n2 in edges:
6            adj_list[n1].append(n2)
7            adj_list[n2].append(n1)
8
9        res = 0
10
11        def dfs(cur, parent):
12            total = values[cur]
13
14            for child in adj_list[cur]:
15                if child != parent:
16                    total += dfs(child, cur)
17            
18            if total % k == 0:
19                nonlocal res
20                res += 1
21            return total
22
23        dfs(0, -1)
24
25        return res
# Last updated: 7/12/2026, 1:12:21 AM
1class Solution:
2    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
3        
4        def dfs(v, res):
5            if v in visited:
6                return 
7            visited.add(v)
8            res.append(v)
9            for nei in adj[v]:
10                dfs(nei, res)
11            return res
12        
13        adj = defaultdict(list)
14        for v1, v2 in edges:
15            adj[v1].append(v2)
16            adj[v2].append(v1)
17
18        res = 0
19        visited = set()
20        for v in range(n):
21            if v in visited:
22                continue
23            
24            component = dfs(v, [])
25            flag = True
26            for v2 in component:
27                if len(component) - 1 != len(adj[v2]):
28                    flag = False
29                    break
30            if flag:
31                res += 1
32
33
34        return res
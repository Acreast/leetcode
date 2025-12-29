# Last updated: 12/30/2025, 12:21:00 AM
1class Solution:
2    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
3        tab = defaultdict(set)
4        for u, v, w in allowed:
5            tab[u, v].add(w)
6
7        def add_neighbor(node):
8            res = ['']
9            for i in range(1, len(node)):
10                eles = tab[(node[i - 1], node[i])]
11                if eles:
12                    res = [a + e for e in eles for a in res]
13                else:
14                    return []
15            return res
16        
17        
18        visited = set()
19
20        def dfs(node):
21            if len(node) == 1:
22                return True
23            if node in visited:
24                return False
25
26            for nxt in add_neighbor(node):
27                if dfs(nxt):
28                    return True
29
30            visited.add(node)
31            return False
32
33        return dfs(bottom)
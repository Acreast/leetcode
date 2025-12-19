# Last updated: 12/19/2025, 9:09:52 PM
1class Solution:
2    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
3        time_map = {}
4        secrets = set([0, firstPerson])
5
6        for src, dest, time in meetings:
7            if time not in time_map:
8                time_map[time] = defaultdict(list)
9            time_map[time][src].append(dest)
10            time_map[time][dest].append(src)
11        
12        def dfs(src, nei):
13            if src in visited:
14                return
15            visited.add(src)
16            secrets.add(src)
17            for n in nei[src]:
18                dfs(n, nei)
19
20        for t in sorted(time_map.keys()):
21            visited = set()
22
23            for src in time_map[t]:
24                if src in secrets:
25                    dfs(src, time_map[t])
26        
27        return list(secrets)
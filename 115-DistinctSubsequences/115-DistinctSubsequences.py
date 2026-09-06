# Last updated: 9/7/2026, 12:59:23 AM
1class Solution:
2    def numDistinct(self, s: str, t: str) -> int:
3        cache = {}
4        def dfs(i,j):
5            if j == len(t):
6                return 1
7            if i == len(s):
8                return 0
9            
10            if (i,j) in cache:
11                return cache[(i,j)]
12
13            if s[i] == t[j]:
14                cache[(i,j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
15            else:
16                cache[(i,j)] = dfs(i + 1, j)
17            return cache[(i,j)]
18
19
20        return dfs(0,0)
# Last updated: 9/29/2026, 11:23:48 PM
1class Solution:
2    def hasValidPath(self, A: list[list[str]]) -> bool:
3        m, n = len(A), len(A[0])
4
5        if ~(m + n) & 1 or A[0][0] == ")" or A[-1][-1] == "(":
6            return False
7
8        @cache
9        def dfs(i, j, x):
10            x += 1 - ((ord(A[i][j]) & 1) << 1)
11
12            if x < 0 or x > (m + n - 1) - (i + j):
13                return False
14
15            if i == m - 1 and j == n - 1:
16                return x == 0
17
18            return (i < m - 1 and dfs(i + 1, j, x)) or \
19                   (j < n - 1 and dfs(i, j + 1, x))
20
21        return dfs(0, 0, 0)
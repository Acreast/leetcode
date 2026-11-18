# Last updated: 11/19/2026, 12:01:01 AM
1class Solution:
2    def minChanges(self, s: str) -> int:
3        res = 0
4        l = 0
5        for r in range(len(s)):
6            if s[l] != s[r]:
7                if r % 2 != 0:
8                    res += 1
9                l = r
10
11        return res
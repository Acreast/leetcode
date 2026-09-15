# Last updated: 9/16/2026, 1:17:11 AM
1class Solution:
2    def maxPalindromes(self, s: str, k: int) -> int:
3        n = len(s)
4        if k == 1: return n
5
6        res = i = 0
7
8        while i <= n - k:
9            for d in (k, k + 1):
10                if i + d <= n and s[i : i + d] == s[i : i + d][::-1]:
11                    res += 1
12                    i += d
13                    break
14            else:
15                i += 1
16
17        return res
# Last updated: 10/10/2026, 12:46:33 AM
1class Solution:
2    def minInsertions(self, s: str) -> int:
3        ans = x = 0
4        i, n = 0, len(s)
5        while i < n:
6            if s[i] == '(':
7                x += 1
8            else:
9                if i < n - 1 and s[i + 1] == ')':
10                    i += 1
11                else:
12                    ans += 1
13                if x == 0:
14                    ans += 1
15                else:
16                    x -= 1
17            i += 1
18        ans += x << 1
19        return ans
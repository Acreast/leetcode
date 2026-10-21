# Last updated: 10/21/2026, 10:49:57 PM
1class Solution:
2    def minOperations(self, s: str) -> int:
3        n = len(s)
4        mn = mx = s[0]
5        isSorted = 1
6
7        for i in range(1, n):
8            if s[i] < s[i - 1]:
9                isSorted = 0
10            mn = min(mn, s[i])
11            mx = max(mx, s[i])
12
13        if isSorted: return 0
14        if n == 2: return -1
15        if s[0] == mn or s[-1] == mx:
16            return 1
17
18        for i in range(1, n - 1):
19            if s[i] == mn or s[i] == mx:
20                return 2
21
22        return 3
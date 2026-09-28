# Last updated: 9/29/2026, 12:27:05 AM
1class Solution:
2    def maxDepth(self, s: str) -> int:
3        res = 0
4        count = 0
5        for c in s:
6            if c == '(':
7                count += 1
8                res = max(count, res)
9            elif c == ')':
10                count -= 1
11        
12        return res
13
14            
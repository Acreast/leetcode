# Last updated: 10/4/2026, 1:43:37 AM
1class Solution:
2    def longestValidParentheses(self, s: str) -> int:
3        stack = [-1]
4        res = 0
5        for i, c in enumerate(s):
6            if c == '(':
7                stack.append(i)
8            else:
9                stack.pop()
10
11                if not stack:
12                    stack.append(i)
13                
14                else:
15                    res = max(res, i - stack[-1])
16
17        return res
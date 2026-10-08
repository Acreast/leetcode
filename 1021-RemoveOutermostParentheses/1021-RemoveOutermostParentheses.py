# Last updated: 10/9/2026, 12:31:08 AM
1class Solution:
2    def removeOuterParentheses(self, s: str) -> str:
3        segment = []
4        res = ""
5        open_count = 0
6        close_count = 0
7        for c in s:
8            if c == "(":
9                open_count += 1
10            else:
11                close_count += 1
12            segment.append(c)
13            if open_count == close_count:
14                segment.pop(0)
15                segment.pop(-1)
16                res += "".join(segment)
17                open_count = 0
18                close_count = 0
19                segment = []
20        
21        return res
22                
23
24
# Last updated: 10/2/2026, 12:05:12 AM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        stack.append(s[0])
5        for i in range(1, len(s)):
6            stack.append(s[i])
7            while stack and len(stack) > 1:
8                if stack[-2] == '(' and stack[-1] == ")":
9                    stack.pop()
10                    stack.pop()
11                elif stack[-2] == '{' and stack[-1] == "}":
12                    stack.pop()
13                    stack.pop()
14                elif stack[-2] == '[' and stack[-1] == "]":
15                    stack.pop()
16                    stack.pop()
17                else:
18                    break
19        
20        if len(stack) == 0:
21            return True
22        else:
23            return False
24
25
26
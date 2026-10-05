# Last updated: 10/6/2026, 12:52:38 AM
1class Solution:
2    def scoreOfParentheses(self, s: str) -> int:
3        stack = [0]
4        res = 0
5
6        for c in s:
7            if c == "(":
8                stack.append(0)
9            else: 
10                val = stack.pop()
11                if val == 0:
12                    stack[-1] += 1
13                else:
14                    stack[-1] += val * 2
15        
16        return stack[0]
17            
18[0,0]
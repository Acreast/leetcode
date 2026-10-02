# Last updated: 10/3/2026, 1:40:04 AM
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        res = []
4        stack = []
5
6        def backtrack(open_count, close_count):
7            
8            if open_count == close_count == n:
9                res.append("".join(stack))
10                return
11            
12            if open_count < n:
13                stack.append("(")
14                backtrack(open_count + 1, close_count)
15                stack.pop()
16            
17            if open_count > close_count:
18                stack.append(")")
19                backtrack(open_count, close_count + 1)
20                stack.pop()
21
22        backtrack(0,0)
23        return res
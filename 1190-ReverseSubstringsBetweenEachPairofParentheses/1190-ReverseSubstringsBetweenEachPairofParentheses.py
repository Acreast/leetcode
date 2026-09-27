# Last updated: 9/28/2026, 12:34:00 AM
1class Solution:
2    def reverseParentheses(self, s: str) -> str:
3        ind_stack = deque()
4        res = []
5        
6        for char in s:
7            if (char == '('):
8                ind_stack.append(len(res))
9            elif (char == ')'):
10                start_ind = ind_stack.pop()
11                res[start_ind:] = res[start_ind:][::-1]
12            else:
13                res.append(char)
14
15        return "".join(res)
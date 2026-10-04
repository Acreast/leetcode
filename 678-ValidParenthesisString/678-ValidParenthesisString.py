# Last updated: 10/5/2026, 12:53:44 AM
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        open_stack = []
4        star_stack = []
5
6        for i, char in enumerate(s):
7            if char == '(':
8                open_stack.append(i)
9            elif char == '*':
10                star_stack.append(i)
11            else:  
12                if open_stack:
13                    open_stack.pop()
14                elif star_stack:
15                    star_stack.pop()
16                else:
17                    return False
18        
19        while open_stack and star_stack:
20            if open_stack.pop() > star_stack.pop():
21                return False
22
23        return len(open_stack) == 0
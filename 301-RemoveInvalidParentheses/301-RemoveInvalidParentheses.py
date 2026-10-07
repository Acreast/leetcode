# Last updated: 10/8/2026, 1:07:15 AM
1class Solution:
2    def removeInvalidParentheses(self, s: str) -> list[str]:
3        def is_valid(s: str) -> bool:
4            balance = 0
5            for char in s:
6                if char == '(':
7                    balance += 1
8                elif char == ')':
9                    balance -= 1
10                    if balance < 0:  # More ')' than '('
11                        return False
12            return balance == 0
13        
14
15        result = []
16        visited = set([s])
17        queue = deque([s])
18        found = False
19        while queue:
20            curr = queue.popleft()
21
22            if is_valid(curr):
23                result.append(curr)
24                found = True
25            
26            if found:
27                continue
28            
29            for i in range(len(curr)):
30                if curr[i] not in '()': continue
31                next_state = curr[:i] + curr[i+1:]
32                if next_state not in visited:
33                    visited.add(next_state)
34                    queue.append(next_state)
35        
36        return result
37
38
39